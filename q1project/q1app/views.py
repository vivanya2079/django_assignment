from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Book
from .forms import BookForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth import logout
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Replace 'home' with the name of your home view
    else:
        form = AuthenticationForm()
    return render(request, 'q1app/login.html', {'form': form})
def home(request):
    return render(request, 'home.html')
def logout_view(request):
    logout(request)
    return redirect('home')

# Create your views here.
