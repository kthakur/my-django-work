from django.shortcuts import render_to_response
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render_to_response('siteroot/list.html')