from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='Main'),
    path('books/', views.Books, name='Books'),
    path('shops/', views.Shops, name='Shops'),
    path('shops/<int:shop_id>/', views.Shopinfo, name='ShopInfo'),
    path('books/<int:book_id>/', views.Bookinfo, name='BookInfo'),
]