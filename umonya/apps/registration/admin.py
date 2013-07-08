from django.contrib import admin
from models import (Registration)

# Ensuring that admin is aware of this class


admin.site.register(Registration)
