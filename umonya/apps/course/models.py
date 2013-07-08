from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.utils import timezone
from time import time
from urllib2 import urlopen
import logging


class Course(models.Model):
    pass
