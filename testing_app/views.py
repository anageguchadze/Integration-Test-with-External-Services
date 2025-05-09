from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(600), name='dispatch')
class EventListView(APIView):

    def get(self, request):
        cached_events = cache.get('events')

        if not cached_events:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            cache.set('events', serializer.data, timeout=600)  
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(cached_events, status=status.HTTP_200_OK)
