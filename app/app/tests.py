from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test if two numbers are added properly"""
        self.assertEqual(add(1,3),4)
