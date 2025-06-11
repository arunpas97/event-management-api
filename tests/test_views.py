import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils.timezone import make_aware
from datetime import datetime
from events.models import Event, Attendee

@pytest.mark.django_db
def test_create_event():
    client = APIClient()
    data = {
        "name": "Event Test",
        "location": "Test Location",
        "start_time": "2025-06-12, 10:00 AM",
        "end_time": "2025-06-12, 05:00 PM",
        "max_capacity": 50
    }
    response = client.post(reverse('event-list-create'), data, format='json')
    assert response.status_code == 201
    assert Event.objects.count() == 1

@pytest.mark.django_db
def test_register_attendee():
    client = APIClient()
    # Use `make_aware` to ensure datetime is timezone-aware
    start_time = make_aware(datetime(2025, 6, 12, 10, 0))
    end_time = make_aware(datetime(2025, 6, 12, 15, 0))
    
    event = Event.objects.create(
        name="Event Test",
        location="Test Location",
        start_time=start_time,
        end_time=end_time,
        max_capacity=50
    )
    data = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post(reverse('register-attendee', args=[event.id]), data, format='json')
    assert response.status_code == 201
    assert Attendee.objects.count() == 1
