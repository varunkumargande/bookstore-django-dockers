from django.contrib import admin

from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
    )
    list_filter = (
        "title",
        "id",
    )
    search_fields = [
        "title",
    ]


admin.site.register(Book, BookAdmin)
