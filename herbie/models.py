from django.db import models
import datetime 

"""class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Author(models.Model):
	salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	headshot = models.ImageField(upload_to='/home/gongura/tmp')

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
	"""
"""
class Note(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	text = models.TextField(blank=True,null=True)

def __unicode__(self):
	return u"Note(%s,%s)" % (self.title, self.slug)

def get_absolute_url(self):
	return u"/note/%s/" % self.slug	
	
 class List(models.Model): 
	 title = models.CharField(max_length=250, unique=True) 
def __unicode_(self): 
	   return self.title 
class Meta: 
	   ordering = ['title'] 
	
PRIORITY_CHOICES = ( 
	 (1, 'Low'), 
	 (2, 'Normal'), 
	 (3, 'High'), 
	) 

class Item(models.Model): 
	 title = models.CharField(max_length=250) 
	 created_date = models.DateTimeField(default=datetime.datetime.now) 
	 priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
	 completed = models.BooleanField(default=False) 
	 todo_list = models.ForeignKey(List) 
def __unicode__(self): 
	   return self.title 
class Meta: 
	   ordering = ['-priority', 'title'] 
	
	"""