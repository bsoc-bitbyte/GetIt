from django.contrib import admin
from .models import Ticket


# Register your models here.
class TicketAdmin(admin.ModelAdmin) :
    list_display = ('event', 'buyer', 'purchase_date', 'status')
    search_fields = ('event', 'buyer', 'purchase_date', 'status')
    list_filter = ('event', 'buyer', 'purchase_date', 'status')

admin.site.register(Ticket, TicketAdmin)