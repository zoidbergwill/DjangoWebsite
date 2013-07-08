from django.shortcuts import render_to_response
from django.template import RequestContext
from models import (BlogCategory, BlogPost)


def blog(request):
    return render_to_response(
        'blog.html',
        context_instance=RequestContext(request))
