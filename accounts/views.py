from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Students').exists():
                return redirect('student_dashboard') # Redirect to student dashboard after login
            else:
                user.groups.filter(name='Librarians').exists()
                return redirect('librarian_dashboard')
            
            #handling invalid login
        return render(request, 'accounts/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'accounts/login.html')    

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']
        role = request.POST['role']    # Get user role from form

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another one.')
            return render(request, 'accounts/register.html')

        # Check if passwords match
        if password != password_confirmation:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/register.html')

        # create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        if role == 'student':
            student_group = Group.objects.get(name='Students')
            student_group.user_set.add(user)
        elif role == 'librarian':
            librarian_group = Group.objects.get(name='Librarians')
            librarian_group.user_set.add(user)   

        messages.success(request, 'Registration successiful! You can now log in.')
        return redirect('login') #Redirect to login after registration
    
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('home') 