from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_model_with_email_successful(self):
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
