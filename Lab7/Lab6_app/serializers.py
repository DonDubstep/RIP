from .models import Book
from rest_framework import serializers

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["pk", 'book_name','author','description', 'price','pic']
        