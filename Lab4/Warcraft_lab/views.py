from django.shortcuts import render

def books(request):
    return render(request, 'books.html', {'books': [
        {'title': 'Том 1', 'id': 1},
        {'title': 'Том 2', 'id': 2},
        {'title': 'Том 3', 'id': 3}
    ]
    })
def book(request, id):
    return render(request, 'book.html', {
        'id': id
    })

