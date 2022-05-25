
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

# Create your views here.



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', { 'books': books })

def books_details(request, book_id):
  book = Book.objects.get(id=book_id)
  return render(request, 'books/detail.html', {'book': book})

class BookCreate(CreateView):
  model = Book
  fields = '__all__'
  success_url= '/books/'

class BookUpdate(UpdateView):
  model = Book
  fields = ['title', 'author', 'type']
 

class BookDelete(DeleteView):
  model = Book
  success_url= '/books/'