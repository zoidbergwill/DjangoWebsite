from django.conf.urls import patterns, include, url

#~ Creating the App importable
urlpatterns = patterns(
	'',
	url(
        r'^$',
        'umonya.apps.main.views.home',
        name='home'),
    url(
        r'^about/$',
        'umonya.apps.main.views.about',
        name='about'),
    url(
        r'^resources/$',
        'umonya.apps.main.views.resources',
        name='resources'),
    url(
        r'^registration/$',
        'umonya.apps.main.views.registration',
        name='registration'),
    url(
        r'^contact/$',
        'umonya.apps.main.views.contact',
        name='contact'),
    url(
        r'^course/$',
        'umonya.apps.main.views.course',
        name='course'),
    url(
        r'^blog/$',
        'umonya.apps.main.views.blog',
        name='blog'),
    url(
        r'^announcements/page(?P<page_number>\d+)$',
    	'umonya.apps.main.views.home',
        name='announcements_page'),
    url(
        r'^announcements/(?P<page_number>\d+)(?P<slug>[^\.]+)$',
    	'umonya.apps.main.views.view_announcement',
        name='view_announcement'),)
