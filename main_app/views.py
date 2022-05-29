from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Accessory
from .forms import ReadingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def index(request):
  books = Book.objects.filter(user=request.user)

  return render(request, 'books/index.html', { 'books': books })

@login_required
def books_details(request, book_id):
  book = Book.objects.get(id=book_id)
  accessorys_book_doesnt_have = Accessory.objects.exclude(id__in = book.accessorys.all().values_list('id'))
  reading_form = ReadingForm()
  return render(request, 'books/detail.html', {'book': book, 'reading_form': reading_form, 'accessorys' : accessorys_book_doesnt_have })
 


class BookCreate(LoginRequiredMixin, CreateView):
  model = Book
  fields = ['title', 'author', 'type']
  success_url= '/books/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
  model = Book
  fields = ['title', 'author', 'type']
 

class BookDelete(LoginRequiredMixin, DeleteView):
  model = Book
  success_url= '/books/'

@login_required
def add_reading(request, book_id):
  form= ReadingForm(request.POST)
  if form.is_valid():
    new_reading = form.save(commit=False)
    new_reading.book_id = book_id
    new_reading.save()
  return redirect('detail', book_id=book_id)
  
class AccessoryList(LoginRequiredMixin, ListView):
  model = Accessory

class AccessoryDetail( LoginRequiredMixin, DetailView):
  model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
  model = Accessory
  fields = ['name', 'type']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
  model = Accessory
  success_url = '/accessorys/'

@login_required
def assoc_accessory(request, book_id, accessory_id):
  Book.objects.get(id=book_id).accessorys.add(accessory_id)
  return redirect('detail', book_id=book_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)