import datetime
import calendar
from django.utils import timezone
from django.test import TestCase
from apps.announcements.models import Announcement


class TestClean(TestCase):
    """ Tests Announcement.is_valid_date by testing dates with known
    results or outputs"""

    def test_is_valid_date_tomorrow(self):
        pub_date = timezone.now().date()
        year = pub_date.year
        month = pub_date.month
        day = pub_date.day + 1
        if day < 1:
            day = calendar.monthrange(year, month - 1)[1]
        elif day > calendar.monthrange(year, month)[1]:
            day = 1
        event_date = datetime.datetime(year, month, day, 12, 0, 0)
        test = Announcement(pub_date=pub_date, event_date=event_date)
        self.assertTrue(test.is_valid_date())

    def test_is_valid_date_yesterday(self):
        pub_date = timezone.now().date()
        year = pub_date.year
        month = pub_date.month
        day = pub_date.day - 1
        if day < 1:
            day = calendar.monthrange(year, month - 1)[1]
        elif day > calendar.monthrange(year, month)[1]:
            day = 1
        event_date = datetime.datetime(year, month, day, 12, 0, 0)
        test = Announcement(pub_date=pub_date, event_date=event_date)
        self.assertFalse(test.is_valid_date())


class TestPageLoading(TestCase):
    """ Tests pages loading correctly in announcements pages """
    def test_empty_page(self):
        num_posts = Announcement.objects.all().count()
        total_pages = num_posts // 5
        total_pages += num_posts % 5 and 1 or 0
        empty_page_num = total_pages + 1

        response = self.client.get("/announcements/page" + str(empty_page_num) + "/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'There are no posts.')

    def test_populated_page(self):
        num_posts = Announcement.objects.all().count()
        total_pages = num_posts // 5
        total_pages += num_posts % 5 and 1 or 0

        if total_pages:
            response = self.client.get("/announcements/page" + str(total_pages) + "/")
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'home.html')
            self.assertNotContains(response, 'There are no posts.')

    def test_home_page1_equal(self):
        # Tests page1 of announcements and Home return same result.
        response_announcements_page1 = self.client.get("/announcements/page1/")
        response_home = self.client.get("/")
        self.assertEqual(
            response_home.context["announcements"],
            response_announcements_page1.context["announcements"])
