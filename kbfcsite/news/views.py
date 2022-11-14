from django.shortcuts import render
from news.author import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpateView, AuthorDeleteView
from news.models import News

# Create your views here.
class NewsListView(AuthorListView):
    model = News


class NewsDetailView(AuthorDetailView):
    model = News


class NewsCreateView(AuthorCreateView):
    model = News
    fields = ['title', 'content']


class NewsUpdateView(AuthorUpateView):
    model = News
    fields = ['title', 'content']


class NewsDeleteView(AuthorDeleteView):
    model = News