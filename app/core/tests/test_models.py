from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager, BaseUserManager


#1 Created a unit test for a user creation with email instead of username
class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Creating a new user with an email is successfull"""
        email = 'asest@gmaasd.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        #user = UserManager.create_user(
            #self,
            #email=email,
            #password=password

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized(self):
        """New user email normalized test"""
        email = 'tSDsft@GMAIL.COM'
        user = get_user_model().objects.create_user(email, "123123")

        self.assertEqual(user.email, email.lower())


    def test_new_user_without_email_rasie_error(self):
        """Test if user created without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "123123")

    def test_create_new_superuser(self):
        """Tests if superuser have been suvessfully created"""
        user = get_user_model().objects.create_superuser(
            "test@1asas.com",
            "password"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
