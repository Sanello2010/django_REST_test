from rest_framework.serializers import ModelSerializer
from appbook.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
