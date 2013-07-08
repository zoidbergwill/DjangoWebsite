from django.contrib import admin
from models import (About, Announcement, Dynamic_Section, Event, Note, Page,
                    Registration, SubEvent)

# Ensuring that admin is aware of this class


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'event_date', 'venue')
    search_fields = ('title', 'body', 'venue')
    list_filter = ('pub_date', )
    ordering = ('pub_date', )
    fields = ('title', 'body', 'event_date', 'venue')
    change_form_template = 'main/admin/change_form.html'


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'date_end', 'date_start')
    ordering = ('date_start', )


class SubEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_event', 'date', 'time')
    ordering = ('date', 'time')

admin.site.register(About)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Dynamic_Section)
admin.site.register(Event, EventAdmin)
admin.site.register(Note)
admin.site.register(Page)
admin.site.register(Registration)
admin.site.register(SubEvent, SubEventAdmin)
