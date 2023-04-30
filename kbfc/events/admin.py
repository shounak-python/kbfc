from django.contrib import admin
from events.models import Event, Venue

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "time", "venue")


class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address")


admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)