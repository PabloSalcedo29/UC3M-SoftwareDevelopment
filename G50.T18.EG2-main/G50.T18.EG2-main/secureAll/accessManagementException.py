class AccessManagementException(Exception):
    def __init__(self, message):
        self.accessMessage = message
        super().__init__(self.accessMessage)

    @property
    def message(self):
        return self.accessMessage

    @message.setter
    def message(self, value):
        self.accessMessage = value
