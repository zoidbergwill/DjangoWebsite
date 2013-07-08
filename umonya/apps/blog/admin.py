from django.contrib import admin
from models import (BlogPost, BlogCategory)

# Ensuring that admin is aware of this class


class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogCategory)
