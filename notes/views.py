#from django.http import HttpResponse
""" from django.shortcuts import render_to_response
from herbie.models import List 


def status_report(request): 
 todo_listing = [] 
 for todo_list in List.objects.all(): 
   todo_dict = {} 
   todo_dict['list_object'] = todo_list 
   todo_dict['item_count'] = todo_list.item_set.count() 
   todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count() 
   #todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100) 
   todo_listing.append(todo_dict) 
 return render_to_response('frontpage.html', { 'todo_listing': todo_listing })

"""

from models import Note
from django.http import HttpResponseRedirect, HttpResponseServerError

def create_note(request):
    error_msg = u"No POST data sent."
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('slug') and post.has_key('title'):
            slug = post['slug']
            if Note.objects.filter(slug=slug).count() > 0:
                error_msg = u"Slug already in use."
            else:
                title = post['title']
                new_note = Note.objects.create(title=title,slug=slug)
                return HttpResponseRedirect(new_note.get_absolute_url())
        else:
            error_msg = u"Insufficient POST data (need 'slug' and 'title'!)"
    return HttpResponseServerError(error_msg)

def update_note(request, slug):
    if request.method == "POST":
        post = request.POST.copy()
        note = Note.objects.get(slug=slug)
        if post.has_key('slug'):
            slug_str = post['slug']
            if note.slug != slug_str:
                if Note.objects.filter(slug=slug_str).count() > 0:
                    error_msg = u"Slug already taken."
                    return HttpResponseServerError(error_msg)
                note.slug = slug_str
        if post.has_key('title'):
            note.title = post['title']
        if post.has_key('text'):
            note.text = post['text']
        note.save()
        return HttpResponseRedirect(note.get_absolute_url())
    error_msg = u"No POST data sent."
    return HttpResponseServerError(error_msg)
