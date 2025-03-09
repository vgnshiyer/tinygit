import os


class Config:
    git_dir = ".tinygit"  # directory for storing git metadata
    index_file = "index"  # file for storing the staging area
    head_file = "HEAD"  # file for storing the current branch
    refs_dir = "refs"  # directory for storing branch references
    objects_dir = "objects"  # directory for storing git objects
    default_branch = "main"  # default branch name

    def __init__(self):
        self.repo_path = os.path.join(os.getcwd(), self.git_dir)
        self.index_path = os.path.join(self.repo_path, self.index_file)
        self.head_path = os.path.join(self.repo_path, self.head_file)
        self.refs_dir = os.path.join(self.repo_path, self.refs_dir)
        self.objects_dir = os.path.join(self.repo_path, self.objects_dir)
