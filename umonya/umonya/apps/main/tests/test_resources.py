import datetime, calendar
from django.utils import timezone
from django.test import TestCase
from umonya.apps.main.models import Event, SubEvent, Note
from django.shortcuts import render

class TestNote(TestCase):
    def test_no_notes(self):
        request = self.client.get('/resources/')
        response = render(request.request, "resources.html", {'notes': []})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources.html')
        self.assertContains(response, 'There are no additional resources available.')

    def test_notes(self):
        notes = [Note(title='Note Title', link='')]
        request = self.client.get('/resources/')
        response = render(request.request, "resources.html", {'notes': notes})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources.html')
        self.assertNotContains(
            response,
            'There are no additional resources available.')
        self.assertContains(response, 'Note Title')

    def test_home_page1_equal(self):
        # Tests page1 of announcements and Home return same result.
        response_announcements_page1 = self.client.get('/announcements/page1')
        response_home = self.client.get('/')
        self.assertEqual(
            response_home.content,
            response_announcements_page1.content)

    def test_no_events(self):
        request = self.client.get('/resources/').request
        events = {}
        response = render(request, "resources.html", {'events': events})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources.html')
        self.assertContains(response, 'There are no scheduled upcoming events.')

    def test_events(self):
        request = self.client.get('/resources/').request
        events = {
        "25 December":[[
            "09:00",
            "Christmas Presents"]],
        "26 December":[[
            "08:00",
            "Boxing Day Breakfast"]]}
        response = render(request, "resources.html", {'events': events})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources.html')
        self.assertNotContains(response, 'There are no scheduled upcoming events.')
        self.assertContains(response, '<h3>25 December')
        self.assertContains(response, '<h3>26 December')
        self.assertContains(response, 'Boxing Day Breakfast')