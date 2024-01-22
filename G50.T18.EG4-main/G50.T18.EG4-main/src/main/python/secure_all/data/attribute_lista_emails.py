from secure_all.access_management_exception import AccessManagementException
from .atributo import Atributo


class ListaEmails(Atributo):

    def __init__(self, attr_value):
        self._validation_pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@](\w+[.])+\w{2,3}$'
        self._error_message = "Email invalid"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        num_emails = 0
        for email in attr_value:
            num_emails = num_emails + 1
            super()._validate(email)
        if num_emails < 1 or num_emails > 5:
            raise AccessManagementException("JSON Decode Error - Email list invalid")
        return attr_value
