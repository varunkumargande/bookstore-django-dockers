from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

from .models import Book
from .serializers import BookSerializer


class BookViewset(ModelViewSet):
    renderer_classes = [
        JSONRenderer,
        XMLRenderer,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filter_fields = (
        "id",
        "title",
    )
    ordering_fields = (
        "id",
        "title",
    )
    search_fields = ("title",)

    def get_permissions(self):
        """Returns the permission based on the type of action"""
        if self.action == "list":
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        """Allow partial updates without mandatory fields"""
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)
