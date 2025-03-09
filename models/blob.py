import os
from models.object import TinyGitObject


class BlobObject(TinyGitObject):
    type = b'blob'

    def __init__(self, path: str):
        self.name = os.path.basename(path)
        with open(path, 'rb') as f:
            self.content = f.read()

    def get_data(self) -> str:
        return str(self.content)
