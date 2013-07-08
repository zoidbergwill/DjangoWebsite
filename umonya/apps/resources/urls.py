from django.conf.urls import patterns, url

#~ Creating the App importable
urlpatterns = patterns('',
    url(r'^resources/$', 'umonya.apps.main.views.resources', name='resources'))
