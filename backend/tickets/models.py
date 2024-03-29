from django.db import models
from events.models import Event

status_enums = [
    ('pending','Pending'),
    ('purchased','Purchased'),
    ('failed','Purchase Failed'),
    ('cancelled','Cancelled'),
]

class Ticket (models.Model) :
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        default=None,
        null=False,
        blank=False,
    )
    buyer = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        default=None,
        null=False,
        blank=False,
    )
    response = models.JSONField(default=dict, blank=True, null=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100,
                              choices=status_enums,
                              default='pending')
    
    @staticmethod
    def create_ticket(event_id, buyer, response):
        event = Event.objects.get(id=event_id)
        ticket = Ticket()
        ticket.event = event
        ticket.buyer = buyer
        ticket.response = response
        ticket.price = event.ticket_price
        ticket.save()
        return ticket
    
    def __str__(self):
        return f'{self.event.title} {self.buyer.first_name} {self.buyer.last_name} - {self.id}'
