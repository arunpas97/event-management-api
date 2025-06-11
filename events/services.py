from .models import Attendee
import pytz
from django.utils.timezone import make_aware
from django.utils.timezone import is_naive

def register_attendee(event, attendee_data):
    """
    Registers an attendee for a given event.
    Raises exceptions if the event is full or duplicate registration is detected.
    """
    if event.attendees.count() >= event.max_capacity:
        raise ValueError("Event is fully booked.")
    
    try:
        attendee = Attendee.objects.create(event=event, **attendee_data)
        return attendee
    except:
        raise ValueError("Duplicate registration is not allowed.")

def validate_event_timings(start_time, end_time):
    """
    Validates event timings to ensure the start_time is before end_time.
    """
    if start_time >= end_time:
        raise ValueError("Start time must be earlier than end time.")

def convert_to_timezone(dt, timezone_str):
    """
    Converts a datetime object to a specific timezone.
    If the datetime is naive, make it timezone-aware first.
    """
    target_tz = pytz.timezone(timezone_str)
    if is_naive(dt):
        dt = make_aware(dt)
    return dt.astimezone(target_tz)
