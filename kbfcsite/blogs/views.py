from django.shortcuts import render
from blogs.author import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpateView, AuthorDeleteView
from blogs.models import Blogs

# Create your views here.
class BlogsListView(AuthorListView):
    model = Blogs


class BlogsDetailView(AuthorDetailView):
    model = Blogs


class BlogsCreateView(AuthorCreateView):
    model = Blogs
    fields = ['title', 'content']


class BlogsUpdateView(AuthorUpateView):
    model = Blogs
    fields = ['title', 'content']


class BlogsDeleteView(AuthorDeleteView):
    model = Blogs