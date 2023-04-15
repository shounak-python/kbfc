from django.urls import path
from member.views import memberlist

app_name = "member"
urlpatterns = [
    path("", memberlist, name="memberlist"),
]