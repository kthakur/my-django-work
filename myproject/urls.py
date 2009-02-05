from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
(r'^admin/(.*)', admin.site.root),
#(r'^(?P<url>first-page/)$',  'django.contrib.flatpages.urls'),
#(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/home/gongura/webapps/static/tinymce/jscripts/tiny_mce' }, ),
#(r'^search/$', 'myproject.search.views.search'),
#(r'^$', 'herbie.views.status_report'),
(r'^notes/$', include('notes.urls')),
(r'^herb/$', include('herbie.urls')),
#(r'^autoc/$', include('autoc.urls')),
(r'^portfolio/$', include('portfolio.urls')),
(r'^$', include('siteroot.urls')),
)
