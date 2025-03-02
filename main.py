import argparse

from commands import InitCmd, StatusCmd, CommitCmd, AddCmd
from tinygit import TinyGit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str)
    parser.add_argument("--message", type=str, required=False)
    args = parser.parse_args()

    tinygit = TinyGit()

    command = args.command
    if command == "init":
        tinygit.set_command(InitCmd())
    elif command == "status":
        tinygit.set_command(StatusCmd())
    elif command == "commit":
        tinygit.set_command(CommitCmd())
    elif command == "add":
        tinygit.set_command(AddCmd())

    print(tinygit.run())


if __name__ == "__main__":
    main()
