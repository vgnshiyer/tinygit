from commands.tinygit_cmd import TinyGitCmd
from config import Config
from exceptions import UninitializedRepositoryError, NoChangesToCommitError
from models.index import Index
from models.tree import TreeObject
from models.commit import CommitObject
from collections import defaultdict


class CommitCmd(TinyGitCmd):
    """
    Commit the changes to the repository.

    - creates the tree and the blob objects
    - creates a new commit object
    - updates the head to point to the new commit
    - clears the staging area
    """

    def __init__(self, message: str):
        self.message = message

    def execute(self, config: Config) -> str:
        if not self.is_repository_initialized(config):
            raise UninitializedRepositoryError

        index = Index(config.index_path)
        index.load()

        if not index.files:
            raise NoChangesToCommitError

        num_files = len(index.files)
        tree_hash = self._create_tree(index, config)
        commit_hash = self._create_commit(tree_hash, self.message, config)

        self._update_head(commit_hash, config)
        index.clear()
        index.save()

        return f"[{commit_hash}] {self.message}" + \
            f"\n{num_files} files changed"

    def _create_tree(self, index: Index, config: Config) -> str:
        """
        Creates the graph
        e.g.
        graph = {
            "/": ["file", "foo/"],
            "foo/": ["bar"]
        }

        Converts into a tree object
        """
        files_to_commit = [(".", file) for file in index.files]

        graph = defaultdict(list)
        while files_to_commit:
            parent, file = files_to_commit.pop()
            parts = file.split("/", 1)
            if len(parts) > 1:
                child = parts[0]
                files_to_commit.append((child, parts[1]))
                graph[parent].append(child)
            else:
                graph[parent].append(parts[0])

        tree = TreeObject(graph, root=".", objects_dir=config.objects_dir)
        return tree.save(config.objects_dir)

    def _create_commit(self, tree_hash: str, message: str, config: Config) -> str:
        parent_commit_hash = self._get_current_commit_hash(config)
        commit = CommitObject(tree_hash, message, parent_commit_hash)
        return commit.save(config.objects_dir)

    def _update_head(self, commit_hash: str, config: Config) -> None:
        current_branch = self._get_current_branch(config)
        with open(config.refs_dir + "/" + current_branch, "w") as f:
            f.write(commit_hash)

        with open(config.head_path, "w") as f:
            f.write(current_branch)
