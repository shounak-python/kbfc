from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about", views.homepage, name="about"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
