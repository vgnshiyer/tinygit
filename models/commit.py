from models.object import TinyGitObject


class CommitObject(TinyGitObject):
    """
    A commit object is a commit in the repository.
    """

    type = b'commit'

    def __init__(self, tree_hash: str, message: str, parent_hash: str | None = None):
        self.tree_hash = tree_hash
        self.message = message
        self.parent_hash = parent_hash

    def get_data(self) -> str:
        return f"tree {self.tree_hash}\n" + \
            (f"parent {self.parent_hash}\n" if self.parent_hash else "") + \
            "\n" + \
            self.message
