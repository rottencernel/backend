from rest_framework.test import APITestCase
from rest_framework import status


class RegistrationTestCase(APITestCase):
    def test_can_register_with_valid_data(self):
        data = {
            'username': 'test',
            'password': 'test',
            'password2': 'test'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_register_with_invalid_data(self):
        data = {
            'username': None,
            'password': 'test',
            'password2': 'test'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

