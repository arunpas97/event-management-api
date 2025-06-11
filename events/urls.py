from django.urls import path
from .views import EventListCreateView, RegisterAttendeeView, EventAttendeeListView

urlpatterns = [
    path('events', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:event_id>/register', RegisterAttendeeView.as_view(), name='register-attendee'),
    path('events/<int:event_id>/attendees', EventAttendeeListView.as_view(), name='event-attendees'),
]
