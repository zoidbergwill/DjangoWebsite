from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.utils import timezone
from time import time
from urllib2 import urlopen
import logging
from django.contrib.auth.models import User


class BlogPost(models.Model):
    '''
        Model for blog posts
        Stores title, body, author
        Date Published set on creation.
    '''
    title = models.CharField(
        max_length=200,
        blank=False)
    body = models.TextField(
        blank=False,)
    pub_date = models.DateField(
        'Date Published',
        editable=False,
        auto_now_add=True)
    author = models.ForeignKey(
        User,
        null=True,
        blank=True)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return u'%s %s' % (self.title, self.pub_date)

    def clean(self):

        # replaces <br>'s and \r\n's with <p>
        if not self.body.startswith("<p>"):
            self.body = "<p>" + self.body

        if not self.body.endswith("</p>"):
            self.body = self.body + "</p>"

        self.body = self.body.replace("\r\n", "</p><p>")
        self.body = self.body.replace("<br>", "</p><p>")
        self.body = self.body.replace("</p><p></p><p>", "</p><p>")

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
        super(BlogPost, self).save()
        logging.debug('Successful save.')


class BlogCategory(models.Model):
    '''
        Model for blog posts
        Stores title, body, author
        Date Published set on creation.
    '''
    name = models.CharField(
        max_length=200)
    post = models.ForeignKey(BlogPost, related_name="category")
