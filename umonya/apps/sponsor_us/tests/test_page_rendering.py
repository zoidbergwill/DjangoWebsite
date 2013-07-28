from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_sponsors(self):
        response = self.client.get("/sponsor_us/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sponsor_us.html")


class TestUrls(TestCase):
    def test_sponsors_url(self):
        url = reverse("apps.sponsor_us.views.sponsor_us")
        self.assertEqual(url, "/sponsor_us/")
