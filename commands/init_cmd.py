import os

from commands.tinygit_cmd import TinyGitCmd
from config import Config


class InitCmd(TinyGitCmd):
    """
    Initialize a new TinyGit repository.

    - initializes the .tinygit directory
    - creates the objects directory for storing git objects
    - creates the refs/heads directory for branches
    - creates the HEAD file for tracking the current branch (default: main)
    - creates the index file for the staging area
    """

    def execute(self, config: Config) -> str:
        os.makedirs(config.repo_path, exist_ok=True)
        os.makedirs(config.refs_dir, exist_ok=True)
        os.makedirs(config.objects_dir, exist_ok=True)

        if not os.path.exists(config.head_path):
            with open(config.head_path, "w") as f:
                f.write(config.default_branch)

        if not os.path.exists(config.index_path):
            with open(config.index_path, "w") as f:
                f.write("")

        return "Initialized empty TinyGit repository in {}".format(config.repo_path)
