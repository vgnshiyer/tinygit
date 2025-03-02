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

    def execute(self, config: Config, file_path: str) -> str:
        if not self.is_repository_initialized(config):
            raise UninitializedRepositoryError

        index = Index(config.index_path)
        index.load()
        index.add_file(file_path)
        index.save()

        return "Added file {} to the staging area".format(file_path)
