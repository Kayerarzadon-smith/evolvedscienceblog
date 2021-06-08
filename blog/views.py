from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views import generic
from .models import Post

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

def ostarine (request):
    ostarine = Post.objects.filter(content__contains="ostarine")
    return render(request, 'blog/ostarine.html', {"ostarine" : ostarine}) 

def lgd_4033 (request):
    lgd4033 = Post.objects.filter(content__contains="LGD 4033")
    return render(request, 'blog/lgd4033.html', {"lgd4033" : lgd4033})   

def AndarineS4 (request):
    andarine = Post.objects.filter(content__contains="andarine s4")
    return render(request, 'blog/AndarineS4.html', {"andarine" : andarine})

def S_23 (request):
    s23 = Post.objects.filter(content__contains="s-23")
    return render(request, 'blog/S-23.html', {"s23" : s23})

def YK11 (request):
    yk11 = Post.objects.filter(content__contains="yk11")
    return render(request, 'blog/YK11.html', {"yk11" : yk11})

def LGD3033 (request):
    lgd3033 = Post.objects.filter(content__contains="lgd3033")
    return render(request, 'blog/LGD3033.html', {"lgd3033" : lgd3033})     

def ACP105 (request):
    acp105 = Post.objects.filter(content__contains="acp105")
    return render(request, 'blog/ACP105.html', {"acp105" : acp105})  
    
def AC262 (request):
    ac262 = Post.objects.filter(content__contains="ac262")
    return render(request, 'blog/AC262.html', {"ac262" : ac262}) 

    