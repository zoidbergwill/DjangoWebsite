from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_announcement_page(self):
        response = self.client.get("/announcements/page1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")


class TestUrls(TestCase):
    def test_home_url(self):
        url = reverse("apps.announcements.views.home")
        self.assertEqual(url, "/")
