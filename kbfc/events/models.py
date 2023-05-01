from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Venue(models.Model):
    name = models.CharField(
        max_length=100, blank=False, null=False, help_text="Name of Venue"
    )

    address = models.TextField(blank=False, null=False, help_text="Address of Venue")

    phone = PhoneNumberField(blank=False, help_text="Phone number with country code")

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = "Venue"
    


class Event(models.Model):
    title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Name of event"
    )

    description = models.CharField(
        max_length=300, blank=False, null=False, help_text="Description of the event"
    )

    date = models.DateField(blank=False, help_text="Date of the event.")

    time = models.TimeField(blank=False, help_text="Time of the event.")

    event_duration = models.SmallIntegerField(
        blank=False, help_text="Duration of the Event"
    )

    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Venue of the event",
        related_name="venue",
    )

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name_plural = "Events"