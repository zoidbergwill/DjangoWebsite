from django.test import TestCase
from apps.about.models import About
from apps.utils.models import Page
import datetime
from django.utils.timezone import utc
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_about(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('about' in response.context)
        self.assertTrue('page_content' in response.context)
        self.assertTemplateUsed(response, "about.html")


class TestPageContent(TestCase):
    def test_about_content(self):
        Page.objects.create(page="about",
                            content="<h1>Umonya heading</h1>")

        page_all = Page.objects.all()

        response = self.client.get("/about/")
        content = response.context['page_content'][page_all.count() - 1]
        self.assertEqual([a.pk for a in response.context['page_content']], [i.pk for i in page_all])
        self.assertEqual(content.page, "about")
        self.assertEqual(content.content, "<h1>Umonya heading</h1>")

    def test_about_bios(self):
        About.objects.create(name="Umonya Name",
                             bios="Umonya Bios",
                             bios_photo="path/2/Um/Photo.png",
                             pub_date=datetime.datetime.utcnow().
                             replace(tzinfo=utc))

        about_all = About.objects.all()

        response = self.client.get("/about/")

        # index never negative because object created above
        content = response.context['about'][about_all.count() - 1]
        self.assertEqual([a.pk for a in response.context['about']], [i.pk for i in about_all])
        self.assertEqual(content.name, "Umonya Name")
        self.assertEqual(content.bios, "Umonya Bios")
        self.assertEqual(content.bios_photo, "path/2/Um/Photo.png")


class TestUrls(TestCase):
    def test_about_url(self):
        url = reverse("apps.about.views.about")
        self.assertEqual(url, "/about/")
