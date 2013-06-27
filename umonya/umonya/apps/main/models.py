from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.utils import timezone
from time import time
from urllib2 import urlopen
import logging


def get_image_path(instance, filename):
    '''
        Returns the file path to store the images which is passed to the
        database
    '''
    return 'img/pic/bios/%s_%s' % (str(time()).replace('.', '_'), filename)


class Announcement(models.Model):
    '''
        Model for announcements
        Stores title, body, event date, venue (can be blank)
        Date Published set on creation.
    '''
    title = models.CharField(
        max_length=200,
        unique=True,
        blank=False)
    body = models.TextField(
        blank=False,)
    pub_date = models.DateField(
        'Date Published',
        auto_now=True)
    event_date = models.DateTimeField(
        'Event Date',
        default=timezone.now(),
        blank=True,
        null=True)
    venue = models.CharField(
        max_length=300,
        default='UCT',
        blank=True,
        null=True)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return u'%s %s' % (self.title, self.pub_date)

    is_valid_date = lambda s: s.event_date.date() >= s.pub_date

    def clean(self):

        if self.event_date:
            if not self.is_valid_date():
                logging.debug('Someone tried to set an invalid date.')
                raise ValidationError(u'Event date is not valid!',
                    code='invalid')

        if self.title.isspace():
            raise ValidationError(u'Title seems to be empty!',
                code='invalid')

        if self.body.isspace():
            raise ValidationError(u'Body seems to be empty!',
                code='invalid')

        logging.debug('Successful clean.')

    def save(self):
        '''
            Custom save function
            Sets Date Published to current time on save.
            Creates slug from title
        '''
        self.slug = self.title.replace(' ', '_')
        super(Announcement, self).save()
        logging.debug('Successful save.')


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
            raise ValidationError(u'Your link seems to be broken!',
                code='invalid')

        result = urlopen(self.link)
        size = result.headers['content-length']

        def sizeof_fmt(num):
            for x in ['bytes','KB','MB','GB']:
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


class About(models.Model):
    '''
        The About Model stores the umonya team personal data i.e. the
        content to be displayed in the \about page
    '''
    name = models.CharField(max_length=200)
    bios = models.TextField()
    bios_photo = models.ImageField(upload_to=get_image_path,
                                   blank=True, null=True)
    pub_date = models.DateTimeField('Date Published')

    def __unicode__(self):
        return self.name


class Page(models.Model):
    '''
        The Page Model is used to populate content in each of the
        individual pages, the content is stored as HTML in the database
    '''
    page = models.CharField(max_length=200)
    content = models.TextField()

    def __unicode__(self):
        return self.page


class Registration(models.Model):
    '''
        Model that generates specific sections in the User Form
    '''
    TYPE_OF_Q = (('CharField', 'CharField'), ('EmailField', 'EmailField'),
                 ('IntegerField', 'IntegerField'), ('TextField', 'TextField'))

    name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=200, choices=TYPE_OF_Q)
    text = models.CharField(max_length=200)
    priority = models.IntegerField()
    required = models.BooleanField()

    def __unicode__(self):
        return self.name


class Dynamic_Section(models.Model):
    '''
        Sections that can be enabled or disabled by admin such
        as registration form and menu
    '''
    section = models.CharField(max_length=200)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.section


class Contact(models.Model):
    pass
