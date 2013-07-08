from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

# Sets custom 404 page
handler404 = 'apps.main.views.custom_404'

urlpatterns = patterns('',
    # Examples:
    url(r"^",include("apps.main.urls")),

    # url(r'^umonya/', include('umonya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon/.ico$', RedirectView.as_view(url='media/img/pic/favicon.ico'))
)
