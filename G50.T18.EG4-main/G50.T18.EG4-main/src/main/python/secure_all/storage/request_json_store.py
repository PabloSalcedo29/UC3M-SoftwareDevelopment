from secure_all.access_manager_config import JSON_FILES_PATH
from secure_all.access_management_exception import AccessManagementException
from .json_store import JsonStore


class RequestJsonStore(JsonStore):
    # pylint: disable =invalid-name
    class __RequestJsonStore(JsonStore):

        _FILE_PATH = JSON_FILES_PATH + "storeRequest.json"
        _ID_FIELD = "_AccessRequest__id_document"

        def add_item(self, item):
            if not self.find_item(item.id_document) is None:
                raise AccessManagementException("id_document found in storeRequest")
            return super().add_item(item)

        def find_access_code(self, access_code, dni):
            request_stored = self.find_item(dni)
            if request_stored is None:
                raise AccessManagementException("DNI is not found in the store")
            from secure_all.data.access_request import AccessRequest
            request_stored_object = AccessRequest(request_stored['_AccessRequest__id_document'],
                                                  request_stored['_AccessRequest__name'],
                                                  request_stored['_AccessRequest__visitor_type'],
                                                  request_stored['_AccessRequest__email_address'],
                                                  request_stored['_AccessRequest__validity'])
            if not request_stored_object.access_code == access_code:
                raise AccessManagementException("access code is not correct for this DNI")
            return request_stored_object

    __instance = None

    def __new__(cls):
        if not RequestJsonStore.__instance:
            RequestJsonStore.__instance = RequestJsonStore.__RequestJsonStore()
        return RequestJsonStore.__instance

    def __getattr__(self, nombre):
        return getattr(self.__instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.__instance, nombre, valor)
