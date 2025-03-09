import os

from commands.tinygit_cmd import TinyGitCmd
from config import Config
from exceptions import UninitializedRepositoryError
from models.index import Index


class AddCmd(TinyGitCmd):
    """
    Add files to the staging area.

    - adds files to the index
    - updates the index file with the new changes
    """

    def __init__(self, path: str):
        self.path = path

    def execute(self, config: Config) -> str:
        if not self.is_repository_initialized(config):
            raise UninitializedRepositoryError

        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File {self.path} not found")

        index = Index(config.index_path)
        index.load()

        if os.path.isdir(self.path):
            for root, _, files in os.walk(self.path):
                for file in files:
                    index.add_file(os.path.join(root, file))
        else:
            index.add_file(self.path)
        index.save()

        return f"Added {self.path} to the staging area"
