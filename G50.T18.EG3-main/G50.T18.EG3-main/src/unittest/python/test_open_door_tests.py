import unittest

from secure_all import AccessManager, AccessManagementException


class MyTestCase(unittest.TestCase):



    def test_open_door(self): #llave correcta y tiempo valido
        my_key = AccessManager()
        result = my_key.get_open_door("b38941756411a4edacd1353bcf36f983a0746dc8b8b9743bb44994a098db92e1")
        self.assertEqual(True, result)


    def test_open_door_resident(self): #llave para resident con dias 0
        my_key = AccessManager()
        result = my_key.get_open_door("90287952a608e23014189e8d109406ee83021d5b150531683152260bbc546897")
        self.assertEqual(True, result)

    def test_open_door_bad(self): #llave expirada o no encontrada
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            result = my_key.get_open_door("fff00d78646ed41a91d60ec2fc1ed326238e510134ca52e5d9b1de5cbdf2b8ab")
        self.assertEqual("Llave no encontrada o expirada", cm.exception.message)

    def test_open_door_wrong_key(self): #llave incorrecta (mal expresada)
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            result = my_key.get_open_door("b389756411a4ed1353bc6f983a0746dc8b8b9743bb44994a098db92e1")
        self.assertEqual("llave incorrecta", cm.exception.message)

    def test_open_door_fake_one(self): #llave correcta pero tiempo expirado ( creamos una segunda get_access con un fichero distinto (fakeLlaves.json)
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            result = my_key.get_open_door_fake("b38941756411a4edacd1353bcf36f983a0746dc8b8b9743bb44994a098db92e1")
        self.assertEqual("Llave no encontrada o expirada", cm.exception.message)







if __name__ == '__main__':
    unittest.main()
