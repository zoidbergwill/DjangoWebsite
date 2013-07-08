from django.contrib import admin
from models import (Event, Note, SubEvent)

# Ensuring that admin is aware of this class


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'date_end', 'date_start')
    ordering = ('date_start', )


class SubEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_event', 'date', 'time')
    ordering = ('date', 'time')


admin.site.register(Event, EventAdmin)
admin.site.register(Note)
admin.site.register(SubEvent, SubEventAdmin)
