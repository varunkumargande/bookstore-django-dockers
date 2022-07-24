from turtle import title
from django.test import TestCase

# Create your tests here.
from snapshottest.django import TestCase

from books.fixtures import BookFactory, UserFactory

class APITestCase(TestCase):
    def test_api_me(self):
        user = UserFactory(email="babluvarun@gmail.com")
        book = BookFactory(author=user, title="hai")
        print(user, book)
        """Testing the API for /me"""
        response = self.client.get(
            "/book",
            content_type="application/json"
        )
        self.assertMatchSnapshot(my_api_response)