from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

from rest_framework import generics



class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateAPiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

