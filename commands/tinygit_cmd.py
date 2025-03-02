import os
from abc import ABC, abstractmethod

from config import Config


class TinyGitCmd(ABC):
    @abstractmethod
    def execute(self, config: Config) -> str:
        raise NotImplementedError

    def is_repository_initialized(self, config: Config) -> bool:
        return os.path.exists(config.repo_path)
