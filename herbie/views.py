""""#from django.http import HttpResponse
from django.shortcuts import render_to_response
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

""""