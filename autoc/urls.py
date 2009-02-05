from django.conf.urls.defaults import *
urlpatterns = patterns('autoc.views',
    (r'^/lookup/$', 'book_lookup'),
)