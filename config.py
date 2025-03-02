import os


class Config:
    git_dir = ".tinygit"
    index_file = "index"
    head_file = "HEAD"
    refs_dir = "refs"
    objects_dir = "objects"
    default_branch = "main"

    def __init__(self):
        self.repo_path = os.path.join(os.getcwd(), self.git_dir)
        self.config_path = os.path.join(self.repo_path, self.config_file)
        self.index_path = os.path.join(self.repo_path, self.index_file)
        self.head_path = os.path.join(self.repo_path, self.head_file)
        self.refs_dir = os.path.join(self.repo_path, self.refs_dir)
        self.objects_dir = os.path.join(self.repo_path, self.objects_dir)
