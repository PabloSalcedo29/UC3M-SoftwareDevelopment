"""Module """
from secure_all.data.access_key import AccessKey
from secure_all.data.access_request import AccessRequest
from .storage.keys_json_store import KeysJsonStore


class AccessManager:
    # pylint: disable=invalid-name
    class __AccessManager:
        """Class for providing the methods for managing the access to a building"""

        def __init__(self):
            pass

        @staticmethod
        def request_access_code(id_card, name_surname, access_type, email_address, days):
            """ this method give access to the building"""
            my_request = AccessRequest(id_card, name_surname, access_type, email_address, days)
            my_request.store_request()
            return my_request.access_code

        @staticmethod
        def get_access_key(keyfile):
            my_key = AccessKey(keyfile)
            my_key.store_keys()
            return my_key.key

        @staticmethod
        def open_door(key):
            keys_storage = KeysJsonStore()
            return keys_storage.is_valid(key)

    __instance = None

    def __new__(cls):
        if not AccessManager.__instance:
            AccessManager.__instance = AccessManager.__AccessManager()
        return AccessManager.__instance

    def __getattr__(self, nombre):
        return getattr(self.__instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.__instance, nombre, valor)
