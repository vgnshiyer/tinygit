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
            self.files = data["files"] if data else []

    def add_file(self, path: str):
        if path not in self.files:
            self.files.append(path)

    def save(self):
        with open(self.index_path, "w") as f:
            yaml.dump({"files": self.files}, f)

    def clear(self):
        self.files = []
