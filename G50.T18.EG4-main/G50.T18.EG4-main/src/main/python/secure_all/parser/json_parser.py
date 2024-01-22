import json
from secure_all.access_management_exception import AccessManagementException


class JsonParser():

    _key_list = []
    _KEY_ERROR_WRONG_FILE = "Wrong file or file path"
    _ERROR_JSON_DECODE = "JSON Decode Error - Wrong JSON Format"
    _KEY_ERROR_WRONG_LABEL = "JSON Decode Error - Wrong label"

    def __init__(self, file):
        self._file = file
        self._json_content = self._parse_json_file()
        self._validate_json()

    def _parse_json_file(self):
        try:
            with open(self._file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise AccessManagementException(self._KEY_ERROR_WRONG_FILE) from ex
        except json.JSONDecodeError as ex:
            raise AccessManagementException(self._ERROR_JSON_DECODE) from ex
        return data

    def _validate_json(self):
        for key in self._key_list:
            if not key in self._json_content:
                raise AccessManagementException(self._KEY_ERROR_WRONG_LABEL)

    @property
    def json_content(self):
        return self._json_content
