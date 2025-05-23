from django.urls import path
from . views import student_dashboard, librarian_dashboard
from . import views
# from .views import login_view, register_view

urlpatterns = [
    path('', views.home, name='home'),
    path('student_dashboard', student_dashboard, name='student_dashboard'),
    path('librarian_dashboard', librarian_dashboard, name='librarian_dashboard'),
]
