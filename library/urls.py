from django.urls import path
from . views import student_dashboard, librarian_dashboard
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import book_list, add_book, edit_book, delete_book
# from .views import login_view, register_view

urlpatterns = [
    path('', views.home, name='home'),
    path('student_dashboard', student_dashboard, name='student_dashboard'),
    path('librarian_dashboard', librarian_dashboard, name='librarian_dashboard'),
    path('books/', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
