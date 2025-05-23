from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

#views here.
def home(request):
    return render(request, 'library/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard')) # Redirect to dashboard after login
        else:
            #handling invalid login
            return render(request, 'library/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'library/login.html')    

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']

        # Check if passwords match
        if password != password_confirmation:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        # create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Registration successiful! You can now log in.')
        return redirect('login') #Redirect to login after registration
    
    return render(request, 'library/register.html')
    