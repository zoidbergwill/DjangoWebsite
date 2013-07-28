from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_resources(self):
        response = self.client.get("/resources/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "resources.html")

    def test_course(self):
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course.html")


class TestUrls(TestCase):
    def test_course_url(self):
        url = reverse("apps.resources.views.course")
        self.assertEqual(url, "/course/")

    def test_resources_url(self):
        url = reverse("apps.resources.views.resources")
        self.assertEqual(url, "/resources/")
