from myproject.polls.models import Poll
from myproject.polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
list_display = ('question', 'pub_date', 'was_published_today')
inlines = [ChoiceInline]
def was_published_today(self):
    return self.pub_date.date() == datetime.date.today()
was_published_today.short_description = 'Published today?'

admin.site.register(Poll, PollAdmin)



