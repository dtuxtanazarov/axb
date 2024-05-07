from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth import logout
# Create your views here.

class List_home_view(ListView):
    model = Post
    template_name = 'home.html'

class Post_detail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'item'

def Logout_view(request):
    logout(request)
    return render(request, 'registration\logout.html')