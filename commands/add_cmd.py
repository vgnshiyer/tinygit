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

    def __init__(self, file_path: str):
        self.file_path = file_path

    def execute(self, config: Config) -> str:
        if not self.is_repository_initialized(config):
            raise UninitializedRepositoryError

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} not found")

        index = Index(config.index_path)
        index.load()

        if os.path.isdir(self.file_path):
            for root, _, files in os.walk(self.file_path):
                for file in files:
                    index.add_file(os.path.join(root, file))
        else:
            index.add_file(self.file_path)
        index.save()

        return "Added file {} to the staging area".format(self.file_path)
