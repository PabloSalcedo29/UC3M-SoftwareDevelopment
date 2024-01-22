from .atributo import Atributo


class FullName(Atributo):

    def __init__(self, attr_value):
        self._validation_pattern = r'^[A-Za-z0-9]+(\s[A-Za-z0-9]+)+'
        self._error_message = "Invalid full name"
        self._attr_value = self._validate(attr_value)
