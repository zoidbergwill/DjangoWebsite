from django.shortcuts import render_to_response
from django.template import RequestContext
from models import (Event, Note, SubEvent)


def resources(request):
    '''
        Renders resources.html view, with links to notes,
        Displays up coming event, with schedule
        Displays soonest event only

        Stores data:
            Event Name

            day 1
                sub events / schedule
                ...
            day 2
                sub events / schedule
                ...
    '''
    notes = Note.objects.order_by('title')

    events = {}
    event_name = ''

    events_query = Event.objects.all().order_by('-date_start')

    if events_query.count():
        events_all = events_query[0]
        sub_events = SubEvent.objects.filter(
            parent_event=events_all).order_by('time')

        event_name = events_all.title

        for i in sub_events:
            date_string = i.date.strftime('%d %B')
            if date_string not in events.keys():
                events[date_string] = []
            sub_event_time = i.time.strftime('%H:%M')
            sub_event_title = i.title
            events[date_string].append([sub_event_time, sub_event_title])

    return render_to_response(
        'resources.html',
        {
            'notes': notes,
            'events': events,
            'event_name': event_name
        },
        context_instance=RequestContext(request))
