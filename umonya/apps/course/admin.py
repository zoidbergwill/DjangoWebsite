from django.contrib import admin
from models import (Course)

# Ensuring that admin is aware of this class


admin.site.register(Course)
