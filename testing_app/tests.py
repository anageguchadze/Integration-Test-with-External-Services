from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.core.cache import cache
from .models import Event

class EventCacheTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('events-list')

        self.event = Event.objects.create(
            title="Sample Event",
            description="Description of event",
            date="2025-05-09T10:00:00Z"
        )

    def test_get_event_and_cache(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        cached_data = cache.get('events')
        self.assertIsNotNone(cached_data)

    def test_event_update_and_cache_refresh(self):
        self.event.title = "Updated Event"
        self.event.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        cached_data = cache.get('events')
        self.assertIsNotNone(cached_data)
        self.assertEqual(cached_data[0]['title'], 'Updated Event')
