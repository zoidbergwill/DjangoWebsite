from django.contrib import admin
from models import (BlogPost, BlogCategory)

# Ensuring that admin is aware of this class


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    fieldsets = [(None, {'fields': [('title', 'category', 'body')]}), ]
    change_form_template = 'blog/change_form.html'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogCategory)
