from django.contrib import admin
from models import (Contact)

# Ensuring that admin is aware of this class


admin.site.register(Contact)
