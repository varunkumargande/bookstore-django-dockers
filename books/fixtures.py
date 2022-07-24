import factory
from authors.models import Author

from books.models import Book


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("title")
    description = "description"
    price = 100

    class Meta:
        model = Book


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    password = factory.Faker("password")

    class Meta:
        model = Author
