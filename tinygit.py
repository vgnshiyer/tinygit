from config import Config
from commands.tinygit_cmd import TinyGitCmd


class TinyGit:
    """
    This is the controller class for TinyGit Commands.
    """
    def __init__(self):
        self.config = Config()
        self.command: TinyGitCmd | None = None

    def set_command(self, command: TinyGitCmd):
        self.command = command

    def run(self) -> str:
        if self.command is None:
            raise ValueError("No command set")

        return self.command.execute(self.config)
