from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from apps.utils.functions import get_image_path


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


class Sponsor(models.Model):
    '''
        Model for sponsors
        Each sponsor includes url, logo, and name
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
            if self.link.contains('://'):
                validate(self.link)
            else:
                validate('http://%s' % (self.link))
        except ValidationError:
            raise ValidationError(
                u'Your link seems to be broken!',
                code='invalid')
