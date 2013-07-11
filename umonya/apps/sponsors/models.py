from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from apps.main.models import get_image_path


class Sponsor(models.Model):
    '''
        Model for links to notes to display a list of notes
        e.g. codecademy or github
        Stores title, and link
        Date Published set on creation.
    '''
    name = models.CharField(
        max_length=200,
        unique=True)
    link = models.URLField()
    pub_date = models.DateField(
        'Date Published',
        auto_now=True)
    photo = models.ImageField(
        upload_to=get_image_path,
        blank=True,
        null=True)

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
