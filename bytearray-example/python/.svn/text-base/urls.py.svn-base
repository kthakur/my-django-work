import os.path

from django.conf.urls.defaults import *

import python.gateway

urlpatterns = patterns('',
    # Example:
    # (r'^python/', include('python.foo.urls')),

    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': python.gateway.images_root}),
    (r'^$', 'python.gateway.gateway.gw'),
    (r'^test/', 'python.gateway.views.get_snapshots'),
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
