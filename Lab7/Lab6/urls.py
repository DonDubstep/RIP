from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from Lab6_app import views as book_views

router = routers.DefaultRouter()
router.register(r'Books', book_views.BooksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

