"""Implements the RequestsJSON Store"""
from secure_all.storage.json_store import JsonStore
from secure_all.cfg.access_manager_config import JSON_FILES_PATH


class KeyTimeStore():

    """Extends JsonStore """
    class __KeyTimeStore(JsonStore):
        # pylint: disable=too-many-arguments,no-self-use,invalid-name, too-few-public-methods
        ID_FIELD = "key"
        _FILE_PATH = JSON_FILES_PATH + "openDoorStore.json"
        _ID_FIELD = ID_FIELD

        def add_item(self, item):
            return super().add_item(item)

    __instance = None

    def __new__(cls):
        if not KeyTimeStore.__instance:
            KeyTimeStore.__instance = KeyTimeStore.__KeyTimeStore()
        return KeyTimeStore.__instance

    def __getattr__ ( self, nombre ):
        return getattr(self.__instance, nombre)

    def __setattr__ ( self, nombre, valor ):
        return setattr(self.__instance, nombre, valor)
