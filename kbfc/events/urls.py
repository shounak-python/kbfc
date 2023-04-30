from django.urls import path
from events.views import eventlist, eventdetail

app_name = "events"
urlpatterns = [
    path("", eventlist, name="eventlist"),
    path("eventdetail/<event_pk>", eventdetail, name="eventdetail"),
]