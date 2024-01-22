"""Module """
from datetime import datetime

import secure_all
import re
import json
from pathlib import Path
import os.path
from .access_key import AccessKey


class AccessManager:
    """Class for providing the methods for managing the access to a building"""

    def __init__(self):
        pass

    @staticmethod
    def validate_dni(dni):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) == 9:
            letra = dni[8]
            dni = dni[:8]
            if letras[int(dni) % 23] == letra:
                return True
        return False

    @staticmethod
    def validardni(id_document):
        dni = isinstance(id_document, str)
        if not dni:
            raise secure_all.AccessManagementException("DNI is not valid")

        if len(id_document) != 9:
            raise secure_all.AccessManagementException("DNI is not valid")

        for i in id_document[:8]:
            if not i.isdigit():
                raise secure_all.AccessManagementException("DNI is not valid")

        if not AccessManager.validate_dni(id_document):
            raise secure_all.AccessManagementException("DNI is not valid")

    @staticmethod
    def validaracceso(access_type):
        if access_type == "Resident" or access_type == "Guest":
            pass
        else:
            raise secure_all.AccessManagementException("Access type is not valid")

    @staticmethod
    def validarnombre(full_name):
        if not re.search("[a-zA-Z][ ][a-zA-Z]", full_name):
            raise secure_all.AccessManagementException("Name is not valid")

    @staticmethod
    def validarcorreo(email_address):
        if not re.search("[a-zA-Z1-9]@uc3m.es", email_address):
            raise secure_all.AccessManagementException("Email is not valid")

    @staticmethod
    def validardias(access_type, days):
        if access_type == "Resident" and days != 0 or access_type == "Guest" and (days < 2 or days > 15):
            raise secure_all.AccessManagementException("Days is not valid")

    @staticmethod
    def lecturaficheros(my_file):
        try:
            with open(my_file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise secure_all.AccessManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise secure_all.AccessManagementException("JSON Decode Error- Wrong JSON Format") from ex
        return data

    @staticmethod
    def escrituraficheros(my_file, listasdatos):
        with open(my_file, "w", encoding="utf-8", newline="") as file:
            json.dump(listasdatos, file, indent=2)

    def request_access_code(self, id_document, full_name, access_type, email_address, days):  # funcion1
        self.validardni(id_document)
        self.validarcorreo(email_address)
        self.validaracceso(access_type)
        self.validardias(access_type, days)
        self.validarnombre(full_name)

        my_code = secure_all.AccessRequest(id_document, full_name, access_type, email_address, days)

        my_file = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/accessCodes.json"

        if os.path.exists(my_file):
            datos = self.lecturaficheros(my_file)

            for k in datos:

                if k["_AccessRequest__id_document"] == id_document:
                    raise secure_all.AccessManagementException("id_document found in accessCodes")

            codigo_acceso = my_code.__dict__
            datos.append(codigo_acceso)

            with open(my_file, "w", encoding="utf-8", newline="") as file:
                json.dump(datos, file, indent=2)

        else:
            codigo_acceso = [my_code.__dict__]
            self.escrituraficheros(my_file, codigo_acceso)
        return my_code.access_code

    @staticmethod
    def validarcodigo(codigo_acceso):
        if len(codigo_acceso) != 32:
            raise secure_all.AccessManagementException("Access Code is not valid")
        if not re.search("[a-z0-9]", codigo_acceso):
            raise secure_all.AccessManagementException("Access Code is not valid")

    def get_access_key(self, keyfile):

        try:
            with open(keyfile, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise secure_all.AccessManagementException("JSON is invalid") from ex
        except json.JSONDecodeError as ex:
            raise secure_all.AccessManagementException("JSON Decode Error- Wrong JSON Format") from ex

        codigo_acceso_entrada = data["AccessCode"]
        documento_identidad = data["DNI"]

        for k in data["NotificationMail"]:
            self.validarcorreo(k)

        self.validardni(documento_identidad)

        my_file = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/accessCodes.json"
        mi_destino = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/storeKeys.json"
        mi_clave = self.lecturaficheros(my_file)

        for m in mi_clave:
            if m["_AccessRequest__id_document"] == documento_identidad:
                nueva_peticion = secure_all.AccessRequest(m["_AccessRequest__id_document"],
                                                          m["_AccessRequest__full_name"],
                                                          m["_AccessRequest__visitor_type"],
                                                          m["_AccessRequest__email_address"],
                                                          m["_AccessRequest__validity"])
                codigo_nuevo = nueva_peticion.access_code
                if codigo_nuevo != codigo_acceso_entrada:
                    raise secure_all.AccessManagementException("Codigo de acceso no es correcto para esta funcion")
                my_key = AccessKey(m["_AccessRequest__id_document"], codigo_nuevo, m["_AccessRequest__email_address"],
                                   m["_AccessRequest__validity"])


                if os.path.exists(mi_destino):
                    datos = self.lecturaficheros(mi_destino)
                    nueva_llave = my_key.__dict__
                    datos.append(nueva_llave)

                    with open(mi_destino, "w", encoding="utf-8", newline="") as file:
                        json.dump(datos, file, indent=2)

                else:
                    nueva_llave = [my_key.__dict__]
                    self.escrituraficheros(mi_destino, nueva_llave)

                return my_key.key

        raise secure_all.AccessManagementException("DNI no encontrado en el almacén")

    @staticmethod
    def leer_fichero_llave(inputfile):
        try:
            with open(inputfile, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise secure_all.AccessManagementException("JSON is invalid") from ex
        except json.JSONDecodeError as ex:
            raise secure_all.AccessManagementException("JSON Decode Error- Wrong JSON Format") from ex
        return data

    @staticmethod
    def check_key(llave):
        regex = '[0-9a-f]{64}'
        if re.search(regex, llave):
            return True
        else:
            raise secure_all.AccessManagementException("llave incorrecta")

    def get_open_door(self, key):
        self.check_key(key)
        mi_archivo = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/storeKeys.json"
        lista_llaves = self.leer_fichero_llave(mi_archivo)

        justnow = datetime.utcnow()
        justnow_timestamp = datetime.timestamp(justnow)

        for k in lista_llaves:
            if k["_AccessKey__key"] == key and (k["_AccessKey__expiration_date"] > justnow_timestamp
                                                or k["_AccessKey__expiration_date"] == 0):
                return True

        raise secure_all.AccessManagementException("Llave no encontrada o expirada")

    def get_open_door_fake(self, key):
        self.check_key(key)
        mi_archivo = str(Path.home()) + "/PycharmProjects/G50.T18.EG3/src/JsonFiles/fakeLlaves.json"
        lista_llaves = self.leer_fichero_llave(mi_archivo)

        justnow = datetime.utcnow()
        justnow_timestamp = datetime.timestamp(justnow)

        for k in lista_llaves:
            if k["_AccessKey__key"] == key and (k["_AccessKey__expiration_date"] > justnow_timestamp
                                                or k["_AccessKey__expiration_date"] == 0):
                return True

        raise secure_all.AccessManagementException("Llave no encontrada o expirada")

