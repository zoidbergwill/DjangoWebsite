from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
import logging


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
        editable=False,
        auto_now_add=True)
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

        # replaces <br>'s and \r\n's with <p>
        if not self.body.startswith("<p>"):
            self.body = "<p>" + self.body

        if not self.body.endswith("</p>"):
            self.body = self.body + "</p>"

        self.body = self.body.replace("\r\n", "</p><p>")
        self.body = self.body.replace("<br>", "</p><p>")
        self.body = self.body.replace("</p><p></p><p>", "</p><p>")

        if self.event_date:
            if not self.is_valid_date():
                logging.debug('Someone tried to set an invalid date.')
                raise ValidationError(
                    u'Event date is not valid!',
                    code='invalid')

        if self.title.isspace():
            raise ValidationError(
                u'Title seems to be empty!',
                code='invalid')

        if self.body.isspace():
            raise ValidationError(
                u'Body seems to be empty!',
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
