from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post, Category
from django.db.models import Q

def home(request):
    context = {
        'posts': Post.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'core/home.html', context)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(
            Q(title__contains=searched) | Q(content__contains=searched)
        )
        return render(request, 'core/search.html', {'searched':searched, 'posts':posts})
    else:
        return render(request, 'core/search.html', {})



class CategoryView(ListView):
    ordering = ['-date_posted']

def CategoryView(request, cat):
    category_posts = Post.objects.filter(category__name=cat)
    return render(request, 'core/categories.html', {'cat':cat.title(), 'category_posts':category_posts})
    

class PostListView(ListView):
    model = Post
    template_name = 'core/home.html'         # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'photos', 'photos2','photos3','photos4','photos5','photos6','photos7','photos8','photos9', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def post_form(request):
        submitted = False
        if request.method == 'POST':
            form = PostCreateView(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['category', 'title', 'content', 'photos', 'photos2','photos3','photos4','photos5','photos6','photos7','photos8','photos9', 'price']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False



def about(request):
    return render(request, 'core/about.html', {'title':'About'})