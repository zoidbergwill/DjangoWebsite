from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_sponsors(self):
        response = self.client.get("/sponsors/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sponsor.html")


class TestUrls(TestCase):
    def test_sponsors_url(self):
        url = reverse("apps.sponsors.views.sponsors")
        self.assertEqual(url, "/sponsors/")
