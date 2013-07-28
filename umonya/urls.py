from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

# Sets custom 404 page
handler404 = 'apps.main.views.custom_404'

urlpatterns = patterns(
    '',
    url(r'^$', 'apps.announcements.views.home',  name='home'),
    url(r'^about/$', 'apps.about.views.about', name='about'),
    url(r'^announcements/page(?P<page_number>\d+)/$', 'apps.announcements.views.home', name='announcements_page'),
    url(r'^announcements/page(?P<page_number>\d+)/(?P<slug>[^\.]+)$', 'apps.announcements.views.view_announcement', name='view_announcement'),
    url(r'^blog/$', 'apps.blog.views.blog', name='blog'),
    url(r'^blog/category/(?P<slug>[^\.]+)$', 'apps.blog.views.blog_category', name='blog_category'),
    url(r'^blog/category/(?P<slug>[^\.]+)/page(?P<page_number>\d+)/$', 'apps.blog.views.blog_category', name='blog_category'),
    url(r'^blog/page(?P<page_number>\d+)/$', 'apps.blog.views.blog', name='blog_page'),
    url(r'^blog/page(?P<page_number>\d+)/(?P<slug>[^\.]+)$', 'apps.blog.views.blog', name='view_blogpost'),
    url(r'^contact/$', 'apps.contact.views.contact', name='contact'),
    url(r'^course/$', 'apps.resources.views.course', name='course'),
    url(r'^registration/$', 'apps.registration.views.registration', name='registration'),
    url(r'^resources/$', 'apps.resources.views.resources', name='resources'),
    url(r'^sponsor_us/$', 'apps.sponsor_us.views.sponsor_us', name='sponsor_us'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon/.ico$', RedirectView.as_view(url='media/img/pic/favicon.ico'))
)
