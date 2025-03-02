import yaml


class Index:
    """
    The data structure to store the state of the staging area.

    format:

    files:
      - file1_path
      - file2_path
      - ...

    """

    def __init__(self, index_path: str):
        self.index_path = index_path
        self.files = []

    def load(self):
        with open(self.index_path, "r") as f:
            data = yaml.safe_load(f)
            self.files = data["files"]

    def add_file(self, file_path: str):
        self.files.append(file_path)

    def save(self):
        with open(self.index_path, "w") as f:
            yaml.dump({"files": self.files}, f)
