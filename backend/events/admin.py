from django.contrib import admin
from .models import Event
# Register your models here.


class EventAdmin(admin.ModelAdmin) :
    list_display = ('title', 'date', 'time', 'location', 'ticket_price', 'event_type')
    search_fields = ('title', 'description', 'location', 'email')
    list_filter = ('event_type', 'date', 'time')

admin.site.register(Event, EventAdmin)