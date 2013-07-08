from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_blog(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog.html")


class TestUrls(TestCase):
    def test_blog_url(self):
        url = reverse("apps.blog.views.blog")
        self.assertEqual(url, "/blog/")
