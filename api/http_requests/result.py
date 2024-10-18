class Result:
    """
    Result class
    """

    def __init__(self, return_value=True, error_message=False):
        if return_value:
            self.is_pass = True
            self.is_fail = False
            self.return_value = return_value
            self.error_message = None
        else:
            self.is_pass = False
            self.is_fail = True
            self.return_value = None
            self.error_message = error_message
