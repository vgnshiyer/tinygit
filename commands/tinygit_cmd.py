import os
from abc import ABC, abstractmethod

from config import Config


class TinyGitCmd(ABC):

    @abstractmethod
    def execute(self, config: Config) -> str:
        raise NotImplementedError

    def is_repository_initialized(self, config: Config) -> bool:
        """Except, init method each command should have a repository initialized.  """
        return os.path.exists(config.repo_path)

    def _get_current_branch(self, config: Config) -> str:
        with open(config.head_path, "r") as f:
            return f.read().strip()

    def _get_current_commit_hash(self, config: Config) -> str | None:
        if not os.path.exists(config.refs_dir + "/" + self._get_current_branch(config)):
            return None

        with open(config.refs_dir + "/" + self._get_current_branch(config), "r") as f:
            return f.read().strip()
