from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView (ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView (DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})

def medical_disclaimer(request):
    return render(request, 'blog/medical_disclaimer.html', {'title':'medical_disclaimer'})    

def affiliate_disclaimer(request):
    return render(request, 'blog/affiliate_disclaimer.html', {'title':'affiliate_disclaimer'}) 
    