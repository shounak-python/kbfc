from django.urls import path, reverse_lazy
from . import views

app_name = "news"
urlpatterns = [
    path("", views.NewsListView.as_view(), name="news_list"),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news_detail"),
    path(
        "create",
        views.NewsCreateView.as_view(success_url=reverse_lazy("news:news_list")),
        name="news_create",
    ),
    path(
        "<int:pk>/update",
        views.NewsUpdateView.as_view(success_url=reverse_lazy("news:news_list")),
        name="news_update",
    ),
    path(
        "<int:pk>/delete",
        views.NewsDeleteView.as_view(success_url=reverse_lazy("news:news_list")),
        name="news_delete",
    ),
]
