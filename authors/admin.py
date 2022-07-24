# from django.contrib import admin

# from .models import Author

# # Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'email',
#     )
#     list_filter = ('email', 'id', )
#     search_fields = ['email',]


# admin.site.register(Author, AuthorAdmin)


# creating custom user modal form than above

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

# Register your models here.


class OwnerAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "account_type")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"fields": ("email", "password1", "password2")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "account_type")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "account_type",
        "is_staff",
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = (
        "id",
        "email",
    )


admin.site.register(get_user_model(), OwnerAdmin)
