from django.urls import path
from members.views import memberlist

app_name = "members"
urlpatterns = [
    path("", memberlist, name="memberlist"),
]