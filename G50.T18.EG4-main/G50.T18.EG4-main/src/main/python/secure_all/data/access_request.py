"""MODULE: access_request. Contains the access request class"""
import json
import hashlib
from secure_all.access_management_exception import AccessManagementException
from secure_all.data.attribute_full_name import FullName
from secure_all.data.attribute_email import EmailCheck
from secure_all.data.attribute_access_type import TipoAcceso
from secure_all.data.attribute_dni_validator import ValidarDNI
from secure_all.storage.request_json_store import RequestJsonStore


class AccessRequest:

    def __init__(self, id_document, full_name, visitor_type, email_address, validity):
        self.__id_document = ValidarDNI(id_document).value
        self.__name = FullName(full_name).value
        self.__visitor_type = TipoAcceso(visitor_type).value
        self.__email_address = EmailCheck(email_address).value
        self.__validity = self.validar_dias(validity, visitor_type)
        self.__time_stamp = 1614962381.90867

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @staticmethod
    def validar_dias(days, access_type):
        """validating the validity days"""
        if not isinstance(days, int):
            raise AccessManagementException("days invalid")
        if (access_type == "Resident" and days == 0) or\
           (access_type == "Guest" and 2 <= days <= 15):
            return days
        raise AccessManagementException("days invalid")

    @property
    def validity(self):
        return self.__validity

    @property
    def name(self):
        """Property representing the name and the surname of
        the person who request access to the building"""
        return self.__name

    @name.setter
    def name(self, value):
        """name setter"""
        self.__name = value

    @property
    def visitor_type(self):
        """Property representing the type of visitor: Resident or Guest"""
        return self.__visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self.__visitor_type = value

    @property
    def email_address(self):
        """Property representing the requester's email address"""
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def id_document(self):
        """Property representing the requester's DNI"""
        return self.__id_document

    @id_document.setter
    def id_document(self, value):
        self.__id_document = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def access_code(self):
        """Property for obtaining the access code according the requirements"""
        return hashlib.md5(self.__str__().encode()).hexdigest()

    def store_request(self):
        request_store = RequestJsonStore()
        request_store.add_item(self)
        del request_store
