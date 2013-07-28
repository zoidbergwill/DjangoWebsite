from django.contrib import admin
from models import About, Sponsor

# Ensuring that admin is aware of this class

admin.site.register(About)
admin.site.register(Sponsor)
