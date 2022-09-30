from http import client
import json
from os import access
from urllib import response
import jwt
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class TestAPI(TestCase):
    def test_register(self):
        client = APIClient()
        testUser = {
            "id":1110449207,
            "primer_nombre": "enfermero",
            "segundo_nombre": "Carlos",
            "primer_apellido": "Carranza",
            "segundo_apellido": "Colorado",
            "email": "enfermero@hotmail.com",
            "no_celular": "3124169036",
            "rol": "enfermero",
            "password": "12345"
        }
        response = client.post('/newUsuario', testUser, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Nuevo usuario agregado")

    def test_login(self):
        client = APIClient()
        testUser = {
            "id":1110449207,
            "primer_nombre": "enfermero",
            "segundo_nombre": "Carlos",
            "primer_apellido": "Carranza",
            "segundo_apellido": "Colorado",
            "email": "enfermero@hotmail.com",
            "no_celular": "3124169036",
            "rol": "enfermero",
            "password": "12345"
        }
        response = client.post('/newUsuario', testUser, format='json')
        
        testLoginData = {
            "email": "enfermero@hotmail.com",
            "password": "12345"
        }
        response = client.post('/login2', testLoginData, format='json')
        tokenData = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in tokenData.keys())
        self.assertTrue('refresh' in tokenData.keys())
        self.assertTrue('id' in tokenData.keys())

    def test_getAllMedico(self):
        client = APIClient()
        testUser = {
            "id":1110449205,
            "primer_nombre": "enfermero",
            "segundo_nombre": "Carlos",
            "primer_apellido": "Carranza",
            "segundo_apellido": "Colorado",
            "email": "enfermero@hotmail.com",
            "no_celular": "3124169036",
            "rol": "enfermero",
            "password": "12345"
        }
        response = client.post('/newUsuario', testUser, format='json')
        
        testUser = {
            "especialidad":"cardiologia",
            "id":1110449205
        }
        response = client.post('/newMedico', testUser, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Nuevo medico agregado")

        