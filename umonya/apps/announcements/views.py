from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Announcement


def home(request, page_number=1):
    '''
        Renders the home.html view which is used as the index page i.e
        url path is www.umonya.org/
    '''
    page_number = int(page_number)
    announcements = Announcement.objects.order_by('-pub_date')
    total_announcements = len(announcements)

    # gets section of announcements wanted for page
    if total_announcements > 5:
        announcements = announcements[(page_number * 5)-5:page_number * 5]
        # get page numbers, and total pages
        total_pages = total_announcements // 5
        total_pages += total_announcements % 5 and 1 or 0
    else:
        announcements = announcements[:total_announcements]
        total_pages = 1
    prev = str(page_number - 1)
    next = str(page_number + 1)
    host = request.get_full_path()
    host_s = host.split('/')
    if len(host_s) > 2:
        if host_s[1] == 'announcements':
            prev = 'page%s' % (prev)
            next = 'page%s' % (next)
            path = ''
    else:
        prev = 'announcements/page%s' % (prev)
        next = 'announcements/page%s' % (next)
        path = 'announcements/'
    return render_to_response(
        'home.html',
        {'announcements': announcements,
        'page_number': page_number,
        'total_pages': total_pages,
        'prev': prev,
        'next': next,
        'path': path},
        context_instance=RequestContext(request))


def view_announcement(request, page_number, slug):
    '''
        Renders the view_announcement.html view which is used
        to show announcements
        i.e. url path is www.umonya.org/announcements/<page_number><slug> .
        The announcement is found by the slug stored in the database
    '''
    announcement = get_object_or_404(Announcement, slug=slug)
    return render_to_response('view_announcement.html', {
        'announcement': announcement,
        'page_number': page_number})
