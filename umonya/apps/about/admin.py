from django.contrib import admin
from models import (About)

# Ensuring that admin is aware of this class

admin.site.register(About)