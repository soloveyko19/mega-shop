class UsernameError(Exception):
    def __init__(self, message: str = ""):
        self.message = message


class UsernameAlreadyTakenError(UsernameError):
    pass

