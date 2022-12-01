from django.test import TestCase
from accounts.models import User
# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
class BasicTest(APITestCase):
    def setUp(self):
        client = APIClient()
        user = User.objects.create_user(email="aman@gmail.com",password="Test1234@")
        self.user = self.client.force_login(user)
        self.token = user.get_tokens_for_user()
        token = self.token['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    def test_get_all_primenumber(self):
        data = {
            "min":1,
            "max":2,
            "method":"Normal"
        }
        response = self.client.post('/prime/',data)
        print(response.json())
        self.assertEqual(response.json()['message'],'ok')
