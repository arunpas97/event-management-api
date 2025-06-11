from rest_framework import serializers
from .models import Event, Attendee

class EventSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(
        input_formats=["%Y-%m-%d, %I:%M %p"],
        format="%Y-%m-%d, %I:%M %p"
    )
    end_time = serializers.DateTimeField(
        input_formats=["%Y-%m-%d, %I:%M %p"],
        format="%Y-%m-%d, %I:%M %p"
    )
    class Meta:
        model = Event
        fields = ['id','name', 'location', 'start_time', 'end_time', 'max_capacity']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("Start time must be earlier than end time.")
        return data

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['name', 'email']
