from django.test import TestCase
from .models import Item


# Create your tests here.
class TestDjango(TestCase):

    def testThis1(self):
        self.assertEqual(1, 1)
