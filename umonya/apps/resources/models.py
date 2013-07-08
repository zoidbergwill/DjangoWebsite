from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.utils import timezone
from urllib2 import urlopen


class Note(models.Model):
    '''
        Model for links to notes to display a list of notes
        e.g. codecademy or github
        Stores title, and link
        Date Published set on creation.
    '''
    title = models.CharField(
        max_length=200,
        unique=True)
    link = models.URLField()
    pub_date = models.DateField(
        'Date Published',
        auto_now=True)
    size = models.CharField(
        max_length=300,
        null=True,
        editable=False)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return u'%s %s' % (self.title, self.pub_date)

    def clean(self):
        validate = URLValidator()

        try:
            if self.link.startswith('http://'):
                validate(self.link)
            else:
                validate('http://%s' % (self.link))
        except ValidationError:
            raise ValidationError(
                u'Your link seems to be broken!',
                code='invalid')

        result = urlopen(self.link)
        size = result.headers['content-length']

        def sizeof_fmt(num):
            for x in ['bytes', 'KB', 'MB', 'GB']:
                if num < 1024.0:
                    return "%3.1f%s" % (num, x)
                num /= 1024.0
            return "%3.1f%s" % (num, 'TB')

        self.size = sizeof_fmt(size)


class Event(models.Model):
    '''
        The Event Model stores upcoming events
        default venue is Abbotts College Century Gate
    '''
    title = models.CharField(
        max_length=200)
    date_start = models.DateField(
        'Start Date',
        default=timezone.now().date())
    date_end = models.DateField(
        'End Date',
        default=timezone.now().date())
    venue = models.CharField(
        max_length=300,
        default="Abbotts College Century Gate",
        blank=True)

    def __unicode__(self):
        return self.title


class SubEvent(models.Model):
    '''
        The SubEvent Model stores each sub event by time within events
        default time is 9:00, or time of last sub event
        default event is latest event
    '''
    title = models.CharField(
        max_length=200)
    date = models.DateField(
        'Date',
        auto_now=True,
        editable=True)
    time = models.TimeField('Time')
    parent_event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.title
