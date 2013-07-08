from django.shortcuts import render_to_response
from django.template import RequestContext


def course(request):
    return render_to_response(
        'course.html',
        context_instance=RequestContext(request))
