class RuntimeErrorWithCode(Exception):
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error Code {code}: {message}')
        self.code = code


error = RuntimeErrorWithCode("OUCH!! An error happened..", 500)
print(error.__doc__)
