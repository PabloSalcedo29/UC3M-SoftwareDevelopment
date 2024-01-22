from datetime import datetime
from secure_all.access_manager_config import JSON_FILES_PATH
from secure_all.access_management_exception import AccessManagementException
from secure_all.data.attribute_key import Key
from .json_store import JsonStore


class KeysJsonStore(JsonStore):
    # pylint: disable =invalid-name
    class __KeysJsonStore(JsonStore):
        _FILE_PATH = JSON_FILES_PATH + "storeKeys.json"
        _ID_FIELD = "_AccessKey__key"

        def is_valid(self, key_to_validate):
            key_object = self.find_item(Key(key_to_validate).value)
            if key_object is None:
                raise AccessManagementException("key is not found or is expired")
            justnow = datetime.utcnow()
            justnow_timestamp = datetime.timestamp(justnow)
            if (key_object["_AccessKey__expiration_date"] > justnow_timestamp) or\
               (key_object["_AccessKey__expiration_date"] == 0):
                return True
            raise AccessManagementException("key is not found or is expired")

    __instance = None

    def __new__(cls):
        if not KeysJsonStore.__instance:
            KeysJsonStore.__instance = KeysJsonStore.__KeysJsonStore()
        return KeysJsonStore.__instance

    def __getattr__(self, nombre):
        return getattr(self.__instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.__instance, nombre, valor)
