from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")


class TestUrls(TestCase):
    def test_contact_url(self):
        url = reverse("apps.contact.views.contact")
        self.assertEqual(url, "/contact/")
