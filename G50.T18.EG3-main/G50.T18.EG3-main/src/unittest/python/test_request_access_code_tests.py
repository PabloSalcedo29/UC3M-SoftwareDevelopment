import unittest
from secure_all import AccessManager, AccessManagementException
from unittest import TestCase
from pathlib import Path
import os.path
from os import remove


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        my_file = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/accessCodes.json"
        print(my_file)
        if os.path.exists(my_file):
            remove(my_file)

    def test_request_access_code_good(self):  # caso válido, se devuelve un código de acceso
        my_code = AccessManager()
        valor = my_code.request_access_code("12345678Z", "Jose Lopez", "Guest", "mail@uc3m.es", 12)
        self.assertEqual("06289798d8e9ad61bae5aebfc6002a02", valor)

    def test_request_access_code_good2(self):
        my_code = AccessManager()
        valor = my_code.request_access_code("05270358T", "Pedro Martin", "Resident", "mail@uc3m.es", 0)
        self.assertEqual("304677d3487ce6cbe3bae2e559e9bf91", valor)

    def test_request_access_code_bad_dni(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("12345678B", "Jose Lopez", "Guest", "mail@uc3m.es", 12)
        self.assertEqual(c_m.exception.message, "DNI is not valid")

    def test_request_access_code_dni_7_digits(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("2222222B", "Jose Lopez", "Guest", "mail@uc3m.es", 12)
        self.assertEqual(c_m.exception.message, "DNI is not valid")

    def test_request_access_code_dni_2_letters(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("22222222BB", "Jose Lopez", "Guest", "mail@uc3m.es", 12)
        self.assertEqual(c_m.exception.message, "DNI is not valid")

    def test_request_access_code_dni_0_letters(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("22222222", "Jose Lopez", "Guest", "mail@uc3m.es", 12)
        self.assertEqual(c_m.exception.message, "DNI is not valid")

    def test_request_access_code_dni_10_length(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("222222222B", "Jose Lopez", "Guest", "mail@uc3m.es", 12)
        self.assertEqual(c_m.exception.message, "DNI is not valid")

    def test_request_access_code_dni_letter_in_first(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("B22222222", "Jose Lopez", "Guest", "mail@uc3m.es", 12)
        self.assertEqual(c_m.exception.message, "DNI is not valid")

    def test_request_access_code_bad_name_surname(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("54364901P", "Pedro", "Resident", "mail@uc3m.es", 0)
        self.assertEqual(c_m.exception.message, "Name is not valid")

    def test_request_access_code_bad_access_type(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("54364901P", "Cristina Cifuentes", "Thief", "mail@uc3m.es", 12)
        self.assertEqual(c_m.exception.message, "Access type is not valid")

    def test_request_access_code_bad_email(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("54364901P", "Pedro Martin", "Resident", "mailuc3m.es", 0)
        self.assertEqual(c_m.exception.message, "Email is not valid")

    def test_request_access_code_bad_resident_days(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("54364901P", "Pedro Martin", "Resident", "mail@uc3m.es", 3)
        self.assertEqual(c_m.exception.message, "Days is not valid")

    def test_request_access_code_bad_guest_days(self):
        my_code = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_code.request_access_code("54364901P", "Pedro Martin", "Guest", "mail@uc3m.es", 20)
        self.assertEqual(c_m.exception.message, "Days is not valid")


if __name__ == '__main__':
    unittest.main()
