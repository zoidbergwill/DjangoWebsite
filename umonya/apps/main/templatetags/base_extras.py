from django import template
from django.core import urlresolvers

register = template.Library()

@register.simple_tag
def navactive(request, views):
    views = ["umonya.apps.main.views." + view for view in views.split()]
    try:
        view = urlresolvers.resolve(request.path).url_name
        return view in views and "active" or ""
    except urlresolvers.Resolver404:
        return ""
    except AttributeError:
        return ""