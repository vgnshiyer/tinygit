import os

from commands.tinygit_cmd import TinyGitCmd
from config import Config
from exceptions import UninitializedRepositoryError
from models.index import Index


class StatusCmd(TinyGitCmd):
    """
    Show the status of the repository.

    - shows the current branch
    - shows the files in the staging area
    - shows the files in the working directory that are not tracked by TinyGit
    """

    def execute(self, config: Config) -> str:
        if not self.is_repository_initialized(config):
            raise UninitializedRepositoryError

        current_branch = self._get_current_branch(config)
        index = Index(config.index_path)
        index.load()

        files_staged_for_commit = index.files
        files_in_working_directory = self._get_files_in_working_directory(config)
        files_not_staged_for_commit = [
            file for file in files_in_working_directory if file not in files_staged_for_commit
        ]

        status = f"On branch {current_branch}\n"

        status += "Changes to be committed:\n"
        status += f"        {files_staged_for_commit}\n"

        status += "Changes not staged for commit:\n"
        status += f"        {files_not_staged_for_commit}\n"

        return status

    def _get_current_branch(self, config: Config) -> str:
        with open(config.head_path, "r") as f:
            return f.read().strip()

    def _get_files_in_working_directory(self, config: Config) -> list[str]:
        return os.listdir(config.repo_path)
