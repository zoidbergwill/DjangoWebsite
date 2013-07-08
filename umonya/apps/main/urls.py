from django.conf.urls import patterns, url

#~ Creating the App importable
urlpatterns = patterns('',
    url(r'^$', 'apps.main.views.home',  name='home'),
    url(r'^about/$', 'apps.main.views.about', name='about'),
    url(r'^resources/$', 'apps.main.views.resources', name='resources'),
    url(r'^registration/$', 'apps.main.views.registration', name='registration'),
    url( r'^contact/$', 'apps.main.views.contact', name='contact'),
    url(r'^course/$', 'apps.main.views.course', name='course'),
    url(r'^blog/$', 'apps.main.views.blog', name='blog'),
    url(r'^announcements/page(?P<page_number>\d+)$', 'apps.main.views.home', name='announcements_page'),
    url(r'^announcements/(?P<page_number>\d+)(?P<slug>[^\.]+)$', 'apps.main.views.view_announcement', name='view_announcement'),)
