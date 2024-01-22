import json
from datetime import datetime


class AccessRequest:
    def __init__(self, idDocument, fullName):
        self.accessName = fullName
        self.accessIdDocument = idDocument
        justnow = datetime.utcnow()
        self.accessTimeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def name(self):
        return self.accessName
    @name.setter
    def name(self, value):
        self.accessName = value

    @property
    def idDocument1(self):
        return self.accessIdDocument

    @name.setter
    def idDocument2(self,value):
        self.accessIdDocument = value
