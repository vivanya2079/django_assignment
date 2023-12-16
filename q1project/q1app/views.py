from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list') 
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

# Create your views here.
