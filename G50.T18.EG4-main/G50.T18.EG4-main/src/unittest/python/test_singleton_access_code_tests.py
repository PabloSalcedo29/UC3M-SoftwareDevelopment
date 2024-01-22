import unittest
from secure_all import AccessManager
from secure_all.data.attribute_dni_validator import ValidarDNI


class MyTestCase(unittest.TestCase):
    def test_singleton_access_manager(self):
        access_manager_1 = AccessManager()
        access_manager_2 = AccessManager()
        access_manager_3 = AccessManager()
        access_manager_4 = AccessManager()
        self.assertEqual(access_manager_1, access_manager_2)
        self.assertEqual(access_manager_2, access_manager_3)
        self.assertEqual(access_manager_3, access_manager_4)

        dni_1 = ValidarDNI("12345678Z").value
        dni_2 = ValidarDNI("12345678Z").value
        self.assertEqual(dni_1, dni_2)


if __name__ == '__main__':
    unittest.main()
