from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Announcement
from apps.utils.functions import get_total_pages


def home(request, page_number=1):
    '''
        Renders the home.html view which is used as the index page i.e
        url path is www.umonya.org/
        or www.umonya.org/announcements/page<page_number>/
    '''
    page_number = int(page_number)
    announcements = Announcement.objects.order_by('-pub_date')
    total_announcements = len(announcements)

    # gets section of announcements wanted for page
    announcements = announcements[((page_number - 1) * 5):page_number * 5]
    total_pages = get_total_pages(total_announcements)

    prev = '/announcements/page%s/' % (str(page_number - 1))
    next = '/announcements/page%s/' % (str(page_number + 1))
    path = '/announcements/page'

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
        i.e. url path is www.umonya.org/announcements/page<page_number>/<slug>
        The announcement is found by the slug stored in the database
    '''
    announcement = get_object_or_404(Announcement, slug=slug)
    return render_to_response('view_announcement.html', {
        'announcement': announcement,
        'page_number': page_number})
