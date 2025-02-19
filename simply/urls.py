"""
URL configuration for simply project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from rest_framework import routers
from simplybooks.views import BookView
from simplybooks.views import AuthorView
from simplybooks.views import Genre_Book_View
from simplybooks.views import GenreView
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'book', BookView, 'book')
router.register(r'genre_book', Genre_Book_View, 'genre_book')
router.register(r'author', AuthorView, 'author')
router.register(r'genre', GenreView, 'genre')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
