from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("about", views.AboutView.as_view(), name="about"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]