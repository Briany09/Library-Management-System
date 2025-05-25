from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import BookForm
from .models import Book



#views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {'books': books})


@login_required(login_url='/accounts/login/')
def student_dashboard(request):
    return render(request, 'library/student_dashboard.html')

@login_required(login_url='/accounts/login/')
def librarian_dashboard(request):
    return render(request, 'library/librarian_dashboard.html')

# Book view adding and editing the books
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html', {'form': form, 'book': book})   

def delete_book(request, book_id): 
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/delete_book.html', {'book': book}) 

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})