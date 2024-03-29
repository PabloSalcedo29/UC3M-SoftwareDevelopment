"""Module AccessManager with AccessManager Class """

from secure_all.data.access_request import AccessRequest
from secure_all.data.key_time import KeyTime
from secure_all.data.access_key import AccessKey
from secure_all.data.access_revoke import AccessRevoke


class AccessManager:

    """AccessManager class, manages the access to a building implementing singleton """

    # pylint: disable=too-many-arguments,no-self-use,invalid-name, too-few-public-methods
    class __AccessManager:
        """Class for providing the methods for managing the access to a building"""

        def request_access_code( self, id_card, name_surname, access_type, email_address, days ):
            """ this method give access to the building"""
            my_request = AccessRequest(id_card, name_surname, access_type, email_address, days)
            my_request.store_request()
            return my_request.access_code

        def get_access_key(self, keyfile):
            """Returns the access key for the access code & dni received in a json file"""
            my_key = AccessKey.create_key_from_file(keyfile)
            my_key.store_keys()
            return my_key.key

        def open_door(self, key):
            """Opens the door if the key is valid an it is not expired"""
            key = KeyTime.configuracion(key)
            key.key_time_store()
            return True

        @staticmethod
        def revoke_key(keyfile):
            my_revoke = AccessRevoke.create_revoke_from_file(keyfile)
            return my_revoke.revocar_llave(keyfile)

    __instance = None

    def __new__( cls ) -> object:
        if not AccessManager.__instance:
            AccessManager.__instance = AccessManager.__AccessManager()
        return AccessManager.__instance
