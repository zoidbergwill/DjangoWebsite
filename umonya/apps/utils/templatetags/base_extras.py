from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def navactive(request, urls):
    try:
        return (request.path in (reverse(url) for url in urls.split())) and "active" or ""
    except:
        return ""
