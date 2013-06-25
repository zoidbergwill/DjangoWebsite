import datetime, calendar
from django.utils import timezone
from django.test import TestCase
from umonya.apps.main.models import Announcement

class TestIsValidDate(TestCase):
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
        event_date = datetime.datetime(year,month,day, 12,0,0)
        test = Announcement(pub_date=pub_date,event_date=event_date)
        self.assertEqual(True, test.is_valid_date())

    def test_is_valid_date_yesterday(self):
        pub_date = timezone.now().date()
        year = pub_date.year
        month = pub_date.month
        day = pub_date.day - 1
        if day < 1:
            day = calendar.monthrange(year, month - 1)[1]
        elif day > calendar.monthrange(year, month)[1]:
            day = 1
        event_date = datetime.datetime(year,month,day, 12,0,0)
        test = Announcement(pub_date=pub_date,event_date=event_date)
        self.assertEqual(False, test.is_valid_date())

class TestIsSpace(TestCase):
    """ Tests Announcement.is_space """

    def test_is_space_title_tab(self):
        test = Announcement(title="\t")
        self.assertEqual(True, test.is_space(test.title))

    def test_is_space_body_tab(self):
        test = Announcement(body="\t")
        self.assertEqual(True, test.is_space(test.body))

    def test_is_space_title_space(self):
        test = Announcement(title=" ")
        self.assertEqual(True, test.is_space(test.title))

    def test_is_space_body_space(self):
        test = Announcement(body=" ")
        self.assertEqual(True, test.is_space(test.body))

    def test_is_space_title_newline(self):
        test = Announcement(title="\n")
        self.assertEqual(True, test.is_space(test.title))

    def test_is_space_body_newline(self):
        test = Announcement(body="\n")
        self.assertEqual(True, test.is_space(test.body))

    def test_is_space_title_string(self):
        test = Announcement(title="Test String")
        self.assertEqual(False, test.is_space(test.title))

    def test_is_space_body_string(self):
        test = Announcement(body="Test String")
        self.assertEqual(False, test.is_space(test.body))