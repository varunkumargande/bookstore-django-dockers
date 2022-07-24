from django.core.management.base import BaseCommand
from authors.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Author.objects.count() == 0:
            email = "root@gmail.com"
            password = "root1234"
            print("Creating account for " + email)
            admin = Author.objects.create_superuser(email=email, password=password, account_type=0)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
