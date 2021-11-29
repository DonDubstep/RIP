from django.shortcuts import render
from .models import Book, Shop

def main(request):
    return render(request, 'index.html')

def Books(request):
    booklist = Book.objects.all()
    context = {
        'booklist': booklist
    }
    return render(request, 'Books.html', context)

def Shops(request):
    shoplist = Shop.objects.all()
    context = {
        'shoplist': shoplist
    }
    return render(request, 'Shops.html', context)

def Shopinfo(request, shop_id):
    shop = Shop.objects.get(id = shop_id)
    context = {
        'name': shop.name,
        'site': shop.site,
        'contact_number': shop.contact_number
    }
    return render(request, 'Shop.html', context)

def Bookinfo(request, book_id):
    book = Book.objects.get(id = book_id)
    shop = Shop.objects.get(id = book.shop.id)
    context = {
        'name': book.name,
        'author': book.author,
        'description': book.description,
        'shop': shop
    }
    return render(request, 'Book.html', context)