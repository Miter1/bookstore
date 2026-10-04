"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add-author/', views.add_author, name='add-author'),
    path('add-book/', views.add_book, name='add-book'),
    path('show-books/', views.show_books, name='show-books'),
    path('show-authors/', views.show_authors, name='show-authors'),
    path('delete-author/<int:author_id>/', views.delete_author, name='delete-author'),
    path('delete-book/<int:book_id>/', views.delete_book, name= 'delete-book'),
    path('add-author/<int:author_id>/', views.show_author, name='show-author'),
    path('edit-author/<int:author_id>/', views.edit_author, name= 'edit-author'),
    path('delete-authors/', views.delete_authors, name='delete-authors'),
    path('edit-book/<int:book_id>', views.edit_book, name='edit-book'),
    path('delete-books/', views.delete_books, name='delete-books'),
    path('show-book/<int:book_id>/', views.show_book, name = 'show-book'), 
    path('send-letter', views.send_letter, name='send-letter'),  
    path('send-review', views.send_review, name='send-review'),                  
]
