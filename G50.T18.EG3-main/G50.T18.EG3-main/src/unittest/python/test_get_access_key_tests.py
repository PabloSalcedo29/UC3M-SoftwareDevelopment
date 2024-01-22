from unittest import TestCase
import unittest
from pathlib import Path
from secure_all import AccessManager, AccessManagementException
import os.path
from os import remove


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        my_file = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/storeKeys.json"
        print(my_file)
        if os.path.exists(my_file):
            remove(my_file)

    def test_get_access_key_good1(self):
        my_file = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/valido_n1.json"
        my_key = AccessManager()
        key = my_key.get_access_key(my_file)
        self.assertEqual("90287952a608e23014189e8d109406ee83021d5b150531683152260bbc546897", key)

    def test_get_access_key_good2(self):
        my_file = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/valido_n2.json"
        my_key = AccessManager()
        key = my_key.get_access_key(my_file)
        self.assertEqual("b38941756411a4edacd1353bcf36f983a0746dc8b8b9743bb44994a098db92e1", key)



    def test_invalido_borrado_n3(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n3.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n6(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n6.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n9(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n9.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n12(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n12.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n15(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n15.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n17(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n17.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n19(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n19.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n21(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n21.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n23(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n23.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n25(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n25.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n27(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n27.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n29(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n29.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n31(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n31.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n33(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n33.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n35(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n35.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n37(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n37.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n39(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n39.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n41(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n41.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n44(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n44.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n47(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n47.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_borrado_n50(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_borrado_n50.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n2(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n2.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n5(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n5.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n8(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n8.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n11(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n11.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n14(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n14.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n43(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n43.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n46(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n46.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n49(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n49.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_duplicado_n52(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_duplicado_n52.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n4(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n4.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n7(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n7.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n10(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n10.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n13(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n13.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n16(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n16.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n18(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n18.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n20(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n20.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n22(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n22.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n24(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n24.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n26(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n26.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n28(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n28.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n30(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n30.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n32(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n32.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n34(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n34.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n36(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n36.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n38(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n38.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n40(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n40.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n42(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n42.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n45(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n45.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n48(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n48.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n51(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n51.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")

    def test_invalido_modifica_n53(self):
        my_file = "/PycharmProjects/G50.T18.EG3/src/JsonFiles/invalido_modifica_n53.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.get_access_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON is invalid")


