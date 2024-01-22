import json
from .accessManagementException import AccessManagementException
from .accessRequest import AccessRequest

class AccessManager:
    def __init__(self):
        pass

    def validate_dni(self, dni):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) == 9:
            letra = dni[8]
            dni = dni[:8]
            if letras[int(dni) % 23] == letra:
                return True
        return False

    def readaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise AccessManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise AccessManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            idDoc = DATA["id"]
            name = DATA["name"]
            req = AccessRequest(idDoc, name)
        except KeyError as e:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") from e
        print("DNI correcto")

        # Close the file
        return req
