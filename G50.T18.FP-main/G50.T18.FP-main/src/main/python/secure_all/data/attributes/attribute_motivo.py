"""Class for validating the reason why you want to revoke the key"""
from secure_all.data.attributes.attribute import Attribute
class Motivo(Attribute):
    """Class for validating the full name with a regex"""
    #pylint: disable=too-few-public-methods

    def __init__( self, attr_value):
        self._validation_pattern = r'^.{1,100}$'
        self._error_message = "Reason is not valid"
        self._attr_value = self._validate(attr_value)
