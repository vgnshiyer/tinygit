from models.blob import BlobObject
from models.object import TinyGitObject


class TreeObject(TinyGitObject):
    """
    A tree object is a directory in the repository.
    """
    type = b'tree'

    children: list[tuple[bytes, str, str]] = []
    name: str = ""

    def __init__(self, graph: dict[str, list[str]], root: str = "", objects_dir: str = ""):
        self.name = root + "/"
        for file_or_dir in graph[root]:
            if file_or_dir not in graph:
                blob = BlobObject(root + "/" + file_or_dir)
                blob.save(objects_dir)
                self.children.append((blob.type, blob.get_hash(), blob.name))
            else:
                tree = TreeObject(graph, file_or_dir, objects_dir)
                tree.save(objects_dir)
                self.children.append((tree.type, tree.get_hash(), tree.name))

    def get_data(self) -> str:
        return "\n".join([
            f"{obj[0]} {obj[1]}\t{obj[2]}"
            for obj in self.children
        ])
