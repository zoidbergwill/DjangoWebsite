from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Sets custom 404 page
handler404 = 'umonya.apps.main.views.custom_404'

urlpatterns = patterns('',
    # Examples:
    url(r"^",include("umonya.apps.main.urls")),

    # url(r'^umonya/', include('umonya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon/.ico$', 'django.views.generic.simple.redirect_to', {'url': 'static/img/pic/favicon.ico'})
)
