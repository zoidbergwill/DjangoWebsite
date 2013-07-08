from django.db import models


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
