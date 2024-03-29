from django.db import models

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
    response = models.JSONField(default=dict)
    purchase_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,
                              choices=status_enums,
                              default='pending')
    
    def __str__(self):
        return f'{self.event.title} {self.buyer.first_name} {self.buyer.last_name}'
