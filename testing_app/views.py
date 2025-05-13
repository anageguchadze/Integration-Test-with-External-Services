from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class EventListView(APIView):
    def get(self, request):
        cached_events = cache.get('events')
        if cached_events:
            return Response(cached_events)

        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        cache.set('events', serializer.data, timeout=600)
        return Response(serializer.data)

