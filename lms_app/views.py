from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import Book_form, Category_form
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = Book_form(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
    
    if request.method == 'POST':
        add_category = Category_form(request.POST)
        if add_category.is_valid():
            add_category.save()
    
    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'form': Book_form(),
        'C_form': Category_form(),
        'allbooks': Book.objects.filter(availble=True).count(),
        'Sbooks': Book.objects.filter(status='sold').count(),
        'Rbooks': Book.objects.filter(status='rented').count(),
        'Abooks': Book.objects.filter(status='available').count(),
    }
    return render(request ,'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    context = {
        'books': search,
        'category': Category.objects.all(),
        'C_form': Category_form(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = Book_form(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = Book_form(instance=book_id)
    context = {
        
        'form': book_save,
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')