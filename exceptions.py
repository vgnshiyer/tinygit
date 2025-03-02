
class TinyGitError(Exception):
    pass


class UninitializedRepositoryError(TinyGitError):
    pass


class NoChangesToCommitError(TinyGitError):
    pass
