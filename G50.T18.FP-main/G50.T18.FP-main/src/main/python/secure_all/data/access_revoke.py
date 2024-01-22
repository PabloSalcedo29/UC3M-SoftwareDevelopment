import json
import secure_all
from secure_all.data.attributes.attribute_key import Key
from secure_all.cfg.access_manager_config import JSON_FILES_PATH
from secure_all.data.attributes.attribute_motivo import Motivo
from secure_all.parser.revoke_json_parser import RevokeJsonParser



class AccessRevoke():
    # pylint: disable=too-many-arguments,no-self-use,invalid-name, too-few-public-methods
    def __init__(self, key, revoke, reason):
        self.__key = key
        self.__revoke = revoke
        self.reason = reason

    @staticmethod
    def lecturaficheros(my_file):
        try:
            with open(my_file, "r", encoding="utf-8", newline="") as file:
                datos = json.load(file)
        except FileNotFoundError as ex:
            raise secure_all.AccessManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise secure_all.AccessManagementException("JSON is invalid") from ex
        return datos

    @classmethod
    def create_revoke_from_file(cls, key_file):
        """Class method from creating an instance of AccessKey
        from the content of a file according to RF2"""
        access_revoke_items = RevokeJsonParser(key_file).json_content
        return cls(access_revoke_items[RevokeJsonParser.KEY],
                   access_revoke_items[RevokeJsonParser.REVOKE],
                   access_revoke_items[RevokeJsonParser.REASON])

    def revocar_llave(self, keyfile):
        try:
            with open(keyfile, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)

        except FileNotFoundError as ex:
            raise secure_all.AccessManagementException("JSON is invalid") from ex
        except json.JSONDecodeError as ex:
            raise secure_all.AccessManagementException("JSON Decode Error - Wrong JSON Format") from ex


        test_key = data["Key"]
        test_revoke = data["Revocation"]
        test_reason = Motivo(data["Reason"]).value
        if test_revoke != "Final" and test_revoke != "Temporal":
            raise secure_all.AccessManagementException("Revocation is not valid")
        store_keys = JSON_FILES_PATH + "storeKeys.json"
        mi_clave = self.lecturaficheros(store_keys)
        if not Key(data["Key"]).value:
            raise secure_all.AccessManagementException("key is not valid")
        for m in mi_clave:
            if m["_AccessKey__key"] == test_key:
                if not Key(m["_AccessKey__key"]).value:
                    raise secure_all.AccessManagementException("key is not valid")
                if m["_AccessKey__revoked_key"] == "False":
                    m["_AccessKey__revoked_key"] = "True"
                    emails_rev = m["_AccessKey__notification_emails"]
                    return emails_rev
                raise secure_all.AccessManagementException("key is not valid")

        raise secure_all.AccessManagementException("La llave ya no se encuentra en storeKeys")
