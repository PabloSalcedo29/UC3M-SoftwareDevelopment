
import unittest
from secure_all import AccessManager, JSON_FILES_PATH
from secure_all.exception.access_management_exception import AccessManagementException


class MyTestCase(unittest.TestCase):

    def test_pf_valido1(self):
        my_file = JSON_FILES_PATH + "pf_valido1.json"
        my_key = AccessManager()
        valor = my_key.revoke_key(my_file)
        self.assertEqual(valor, ['mail1@uc3m.es', 'mail2@uc3m.es'])


    def test_pf_valido2(self):
        my_file = JSON_FILES_PATH + "pf_valido2.json"
        my_key = AccessManager()
        valor = my_key.revoke_key(my_file)
        self.assertEqual(valor, ['mail1@uc3m.es', 'mail2@uc3m.es'])





    def test_pf_comillasdolar(self):
        my_file = JSON_FILES_PATH + "pf_comillasdolar.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_comillasduplicadas(self):
        my_file = JSON_FILES_PATH +"pf_comillasduplicadas.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_datos2duplicados(self):
        my_file = JSON_FILES_PATH +"pf_datos2duplicados.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_duplicado1llave(self):
        my_file = JSON_FILES_PATH +"pf_duplicado1llave.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_duplicado2llave(self):
        my_file = JSON_FILES_PATH +"pf_duplicado2llave.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_estructurakeymala(self):
        my_file = JSON_FILES_PATH +"pf_estructurakeymala.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_etiq3duplicada(self):
        my_file = JSON_FILES_PATH +"pf_etiq3duplicada.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_faltaigualador1(self):
        my_file = JSON_FILES_PATH +"pf_faltaigualador1.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_faltakey(self):
        my_file = JSON_FILES_PATH +"pf_faltakey.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong label")

    def test_pf_faltallave1(self):
        my_file = JSON_FILES_PATH +"pf_faltallave1.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_faltallave2(self):
        my_file = JSON_FILES_PATH +"pf_faltallave2.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_faltancomillas(self):
        my_file = JSON_FILES_PATH +"pf_faltancomillas.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_faltandatos3(self):
        my_file = JSON_FILES_PATH +"pf_faltandatos3.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_faltarazon(self):
        my_file = JSON_FILES_PATH +"pf_faltarazon.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong label")

    def test_pf_faltarevocar(self):
        my_file = JSON_FILES_PATH +"pf_faltarevocar.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong label")

    def test_pf_faltaseparador1(self):
        my_file = JSON_FILES_PATH +"pf_faltaseparador1.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_faltavalorkey(self):
        my_file = JSON_FILES_PATH +"pf_faltavalorkey.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "key is not valid")

    def test_pf_faltavalorrevocar(self):
        my_file = JSON_FILES_PATH +"pf_faltavalorrevocar.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "Revocation is not valid")

    def test_pf_igualador1doble(self):
        my_file = JSON_FILES_PATH +"pf_igualador1doble.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_igualador1dolar(self):
        my_file = JSON_FILES_PATH +"pf_igualador1dolar.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_keymala(self):
        my_file = JSON_FILES_PATH +"pf_keymala.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong label")

    def test_pf_llavedolar1(self):
        my_file = JSON_FILES_PATH +"pf_llavedolar1.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_llavedolar2(self):
        my_file = JSON_FILES_PATH +"pf_llavedolar2.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_motivo(self):
        my_file = JSON_FILES_PATH +"pf_motivo.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "Reason is not valid")

    def test_pf_nohaydata(self):
        my_file = JSON_FILES_PATH +"pf_nohaydata.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong label")

    def test_pf_razonmala(self):
        my_file = JSON_FILES_PATH +"pf_razonmala.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong label")

    def test_pf_revocarmalo(self):
        my_file = JSON_FILES_PATH +"pf_revocarmalo.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong label")

    def test_pf_separador1doble(self):
        my_file = JSON_FILES_PATH +"pf_separador1doble.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_separador1dolar(self):
        my_file = JSON_FILES_PATH +"pf_separador1dolar.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_valor1duplicado(self):
        my_file = JSON_FILES_PATH +"pf_valor1duplicado.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_valor2borrados(self):
        my_file = JSON_FILES_PATH +"pf_valor2borrados.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_valor3modificados(self):
        my_file = JSON_FILES_PATH +"pf_valor3modificados.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_pf_valorkeymalexp(self):
        my_file = JSON_FILES_PATH +"pf_valorkeymalexp.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "key is not valid")

    def test_pf_valorrevocarmalo(self):
        my_file = JSON_FILES_PATH +"pf_valorrevocarmalo.json"
        my_key = AccessManager()
        with (self.assertRaises(AccessManagementException)) as c_m:
            my_key.revoke_key(my_file)
        self.assertEqual(c_m.exception.message, "Revocation is not valid")







if __name__ == '__main__':
    unittest.main()
