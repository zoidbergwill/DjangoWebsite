from django.shortcuts import render_to_response
from django.template import RequestContext


def sponsor_us(request):
    '''
        Renders sponsor.html view, which allows sponsors to make donations
        Each sponsor will be able to provie a url, logo, and name.
        Only the name will be required.
    '''
    return render_to_response(
        'sponsor_us.html',
        {
        },
        context_instance=RequestContext(request))
