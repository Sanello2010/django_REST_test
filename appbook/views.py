from django.shortcuts import render
from appbook.serializer import BookSerializer, BookCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

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


class BookCreateView(CreateAPIView):
    serializer_class = BookCreateSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookCreateSerializer
    queryset = Book.objects.all()
# Create your views here.
