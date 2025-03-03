import argparse

from commands import InitCmd, StatusCmd, CommitCmd, AddCmd
from tinygit import TinyGit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str)
    parser.add_argument("--message", type=str, required=False)
    parser.add_argument("--file", type=str, required=False)
    args = parser.parse_args()

    tinygit = TinyGit()

    command = args.command
    if command == "init":
        tinygit.set_command(InitCmd())
    elif command == "status":
        tinygit.set_command(StatusCmd())
    elif command == "commit":
        if not args.message:
            raise ValueError("Message is required for commit command")
        tinygit.set_command(CommitCmd(message=args.message))
    elif command == "add":
        if not args.file:
            raise ValueError("File is required for add command")
        tinygit.set_command(AddCmd(file_path=args.file))

    print(tinygit.run())


if __name__ == "__main__":
    main()
