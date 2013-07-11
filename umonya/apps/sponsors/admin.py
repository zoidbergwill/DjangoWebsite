from django.contrib import admin
from models import (Sponsor)

# Ensuring that admin is aware of this class

admin.site.register(Sponsor)
