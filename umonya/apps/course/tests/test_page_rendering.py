from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_course(self):
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course.html")


class TestUrls(TestCase):
    def test_course_url(self):
        url = reverse("apps.course.views.course")
        self.assertEqual(url, "/course/")
