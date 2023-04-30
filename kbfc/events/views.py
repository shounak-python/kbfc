from django.shortcuts import render
from events.models import Event
import calendar

# Create your views here.


def eventlist(request):
    event_obj = Event.objects.all().order_by("-pk")
    print(event_obj)
    ctx = {"event_obj": event_obj}
    return render(request, "events/eventlist.html", ctx)


def eventdetail(request, event_pk: int):
    event_obj = Event.objects.get(pk=event_pk)
    day_of_week = calendar.day_name[event_obj.date.weekday()]
    ctx = {"event_obj": event_obj, "day_of_week": day_of_week}
    return render(request, "events/eventdetail.html", ctx)