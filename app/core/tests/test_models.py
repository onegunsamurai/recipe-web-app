from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager, BaseUserManager

from core import models

def sample_user(email="test@test.com", password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)



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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name="Cucumber"
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/recipe/{uuid}.jpg'

        self.assertEqual(file_path, exp_path)
