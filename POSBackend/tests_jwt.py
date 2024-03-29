from django.test import TestCase
from django.contrib.auth.models import User
import json

test_users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"},
    {"username": "user4", "password": "password4"},
]

class LoginTest(TestCase):
    def setUp(self):
        for user in test_users:
            new_user = User.objects.create(username=user["username"])
            new_user.set_password(user["password"])
            new_user.save()

    def test_login(self):
        USER1 = test_users[0]
        res = self.client.post('/api/token',
                               data=json.dumps({
                                   'username': USER1["username"],
                                   'password': USER1["password"],
                               }),
                               content_type='application/json',
                               )
        result = json.loads(res.content)
        self.assertTrue("access" in result)