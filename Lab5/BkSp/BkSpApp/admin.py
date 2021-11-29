from django.contrib import admin

from .models import Book, Shop

admin.site.register(Shop)
admin.site.register(Book)