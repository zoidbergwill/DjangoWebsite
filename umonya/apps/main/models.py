from django.db import models
from time import time


def get_image_path(instance, filename):
    '''
        Returns the file path to store the images which is passed to the
        database
    '''
    return 'img/pic/bios/%s_%s' % (str(time()).replace('.', '_'), filename)


class Dynamic_Section(models.Model):
    '''
        Sections that can be enabled or disabled by admin such
        as registration form and menu
    '''
    section = models.CharField(max_length=200)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.section


class Page(models.Model):
    """
        The Page Model is used to populate content in each of the
        individual pages, the content is stored as HTML in the database
    """
    page = models.CharField(max_length=200)
    content = models.TextField()

    def __unicode__(self):
        return self.page
