from django.shortcuts import render
from django.http import HttpResponse
from appbook.serializer import BookSerializer
from rest_framework.generics import CreateAPIView, ListAPIView

from appbook.models import Book


def hello(request):
    response = {'name': 'Alexander', 'title': 'hodor', 'user': 'Oleg'}
    return render(request, 'index.html', response)


def world(request):
    response = {'one': 'one', 'two': 'two', 'three': 'three',
                'count': ['four', 'five', 'six']}
    return render(request, 'world.html', response)


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
# Create your views here.
