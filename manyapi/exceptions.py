class ManyAPIErrors(Exception):
    def __init__(self, message:str=None):
        if message is None:
            message = 'An unknown error has occurred within ManyAPI.'
        super().__init__(message)

class RequestsErrors(ManyAPIErrors):
    def __init__(self, error:str):
        super().__init__(error)