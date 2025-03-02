import hashlib
import os


class TinyGitObject:
    """
    A TinyGit object is a blob, tree, or commit.
    """

    type: bytes = b'Unknown'

    def get_data(self) -> str:
        raise NotImplementedError

    def serialize(self) -> bytes:
        data = self.get_data().encode()
        content = self.type + b' ' + str(len(data)).encode() + b'\x00' + data
        return content

    def get_hash(self) -> str:
        content = self.serialize()
        return hashlib.sha1(content).hexdigest()

    def save(self, objects_dir: str) -> str:
        content = self.serialize()
        hash = self.get_hash()
        path = os.path.join(objects_dir, hash)
        with open(path, 'wb') as f:
            f.write(content)

        return hash
