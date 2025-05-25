from django.urls import path
from . import views
from .views import login_view, logout_view, register_view

urlpatterns = [
    # path('', views.home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    # path('dashboard/', dashboard_view, name='dashboard'),
]