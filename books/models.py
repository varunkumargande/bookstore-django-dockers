from django.utils import timezone

from django.db import models

from authors.models import Author

# Create your models here.
class AbstractBook(models.Model):
    """docstring for AbstractBook"""

    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True, default="")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, default="", related_name="book_author"
    )
    # considering the german euro currency
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to="images/", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%d - %s" % (
            self.pk,
            self.title,
        )

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(AbstractBook, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Book(AbstractBook):
    class Meta:
        ordering = ("-id",)
