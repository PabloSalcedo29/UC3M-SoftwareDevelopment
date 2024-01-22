import re
from secure_all.access_management_exception import AccessManagementException


class Atributo():

    """representa un atributo genérico"""
    _attr_value = ""
    _validation_pattern = r""
    _error_message = ""

    def _validate(self, attr_value):
        if not isinstance(attr_value, str):
            raise AccessManagementException(self._error_message)
        if not re.fullmatch(self._validation_pattern, attr_value):
            raise AccessManagementException(self._error_message)
        return attr_value

    @property
    def value(self):
        return self._attr_value

    @value.setter
    def value(self, attr_value):
        self._attr_value = attr_value
