from django.contrib import admin
from models import (Announcement)

# Ensuring that admin is aware of this class


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'event_date', 'venue')
    search_fields = ('title', 'body', 'venue')
    list_filter = ('pub_date', )
    ordering = ('pub_date', )
    fields = ('title', 'body', 'event_date', 'venue')
    change_form_template = 'main/change_form.html'


admin.site.register(Announcement, AnnouncementAdmin)
