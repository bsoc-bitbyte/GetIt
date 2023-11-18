from django.contrib import admin
from .models import Event, Event_Form
# Register your models here.


class EventAdmin(admin.ModelAdmin) :
    list_display = ('title', 'date', 'time', 'location', 'ticket_price', 'event_type')
    search_fields = ('title', 'description', 'location', 'email')
    list_filter = ('event_type', 'date', 'time')

class Event_FormAdmin(admin.ModelAdmin) :
    list_display = ('event', 'form_fields')
    search_fields = ('event', 'form_fields')
    list_filter = ('event', 'form_fields')

admin.site.register(Event_Form, Event_FormAdmin)

admin.site.register(Event, EventAdmin)