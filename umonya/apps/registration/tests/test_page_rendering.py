from django.test import TestCase
from apps.utils.models import Dynamic_Section
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_registration(self):
        Dynamic_Section.objects.create(section="registration", enabled=True)
        response = self.client.get("/registration/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration.html")


class TestPageContent(TestCase):
    def test_registration_open(self):
        Dynamic_Section.objects.create(section="registration", enabled=True)
        response = self.client.get("/registration/")
        self.assertTrue("section" in response.context)
        self.assertEqual(response.context["section"].enabled, True)
        self.assertContains(response, "</form>")
        self.assertNotContains(response, "registration has closed")

    def test_registration_closed(self):
        Dynamic_Section.objects.create(section="registration", enabled=False)
        response = self.client.get("/registration/")
        self.assertTrue("section" in response.context)
        self.assertEqual(response.context["section"].enabled, False)
        self.assertNotContains(response, "</form>")
        self.assertContains(response, "registration has closed")


class TestUrls(TestCase):
    def test_registration_url(self):
        url = reverse("apps.registration.views.registration")
        self.assertEqual(url, "/registration/")
