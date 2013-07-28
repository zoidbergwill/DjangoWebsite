from django.shortcuts import render_to_response
from django.template import RequestContext
from models import About, Sponsor
from apps.utils.models import Page


def about(request):
    about = About.objects.all()
    page_content = Page.objects.all().filter(page='about')
    sponsors = Sponsor.objects.all()
    return render_to_response(
        'about.html',
        {
            'about': about,
            'page_content': page_content,
            'sponsors': sponsors,
        },
        context_instance=RequestContext(request))
