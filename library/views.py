from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



#views here.
def home(request):
    return render(request, 'library/index.html')

@login_required(login_url='/accounts/login/')
def student_dashboard(request):
    return render(request, 'library/student_dashboard.html')

@login_required(login_url='/accounts/login/')
def librarian_dashboard(request):
    return render(request, 'library/librarian_dashboard.html')


    