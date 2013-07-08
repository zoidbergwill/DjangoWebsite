from django.db import models
from apps.main.models import get_image_path


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
