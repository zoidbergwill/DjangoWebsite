from django.shortcuts import render_to_response
from django.template import RequestContext
from models import (Sponsor)


def sponsors(request):
    '''
        Renders sponsor.html view, with list of sponsors
        Each sponsor includes url, logo, and name

    '''
    sponsors = Sponsor.objects.all()
    return render_to_response(
        'sponsor.html',
        {
            'sponsors': sponsors,
        },
        context_instance=RequestContext(request))


def sponsor_a_child(request):
    '''
        Renders sponsor.html view, with list of sponsors
        Each sponsor includes url, logo, and name

    '''
    sponsors = Sponsor.objects.all()
    return render_to_response(
        'sponsor_pay.html',
        {
            'sponsors': sponsors,
        },
        context_instance=RequestContext(request))
