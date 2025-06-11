from django.db import models
from django.core.exceptions import ValidationError

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time.")

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendees")
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        unique_together = ("event", "email")

    def __str__(self):
        return f"{self.name} ({self.email})"
