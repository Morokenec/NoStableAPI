class Settings:
    def __init__(self, error:int, timeout:int):
        self.error = error
        self.timeout = timeout
    
    def edit_error(self, count):
        self.error - count

    def get_error(self):
        return self.error
        