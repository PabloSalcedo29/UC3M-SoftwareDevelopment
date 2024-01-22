from datetime import datetime
import json
from secure_all.data.access_key import AccessKey
from secure_all.storage.key_time_store import KeyTimeStore


class KeyTime:
    # pylint: disable=too-many-arguments,no-self-use,invalid-name, too-few-public-methods
    def __init__(self, key):
        just_now = datetime.utcnow()
        self.__issued_at = datetime.timestamp(just_now)
        self.__key = key

    def __str__(self):
        return "KeyTime:" + json.dumps(self.__dict__)

    @property
    def key(self):
        """Property that represent the key"""
        return self.__key

    @key.setter
    def key(self, value):
        """Setter of the key value"""
        self.__key = value

    def key_time_store(self):
        """Storing the key in the keys store """
        key_time_store = KeyTimeStore()
        key_time_store.add_item(self)

    @classmethod
    def configuracion(cls, key):
        AccessKey.create_key_from_id(key).is_valid()
        return cls(key)
