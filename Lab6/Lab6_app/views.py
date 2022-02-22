from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BooksSerializer
from .models import Book

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

