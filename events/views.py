from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .services import register_attendee, validate_event_timings,convert_to_timezone
from rest_framework.generics import ListAPIView
from .pagination import AttendeePagination

class EventListCreateView(APIView):
    def get(self, request):
        events = Event.objects.filter(start_time__gt=timezone.now())
        timezone_str = request.query_params.get('timezone', 'UTC')

        for event in events:
        	event.start_time = convert_to_timezone(event.start_time, timezone_str)
        	event.end_time = convert_to_timezone(event.end_time, timezone_str)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new event",
        request_body=EventSerializer,  # This tells Swagger about the required fields
        responses={201: EventSerializer, 400: "Bad Request"}
    )
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
        	try:
        		validate_event_timings(serializer.validated_data['start_time'], serializer.validated_data['end_time'])
        		serializer.save()
        		return Response(serializer.data, status=status.HTTP_201_CREATED)
        	except ValueError as e:
        		return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAttendeeView(APIView):
	@swagger_auto_schema(
		operation_description="Register a new attendee",
		request_body=AttendeeSerializer,
		responses={201: AttendeeSerializer, 400: "Bad Request"}
	)
	def post(self, request, event_id):
		event = get_object_or_404(Event, id=event_id)
		serializer = AttendeeSerializer(data=request.data)

		if serializer.is_valid():
			try:
				attendee = register_attendee(event, serializer.validated_data)
				return Response(AttendeeSerializer(attendee).data, status=status.HTTP_201_CREATED)
			except ValueError as e:
				return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventAttendeeListView(ListAPIView):
    serializer_class = AttendeeSerializer
    pagination_class = AttendeePagination

    def get_queryset(self):
        event = get_object_or_404(Event, id=self.kwargs['event_id'])
        return event.attendees.all()