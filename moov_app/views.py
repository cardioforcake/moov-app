from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render

# from django.http import HttpResponse
# from .models import Deck, Card 
# from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = "Invalid sign up - Try again"
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form, 'error_message' : error_message})

def greeting(request):
    return render(request, 'greeting.html')

def home(request):
    return render(request, 'home.html')