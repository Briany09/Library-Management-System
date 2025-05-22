from django.shortcuts import render

#views here.
def home(request):
    return render(request, 'library/index.html')
