from django.db import models
from tickets.models import Ticket
from accounts.models import Account
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


ORDER_STATUS = (
    ('PENDING', 'Pending'),
    ('COMPLETED', 'Completed'),
    ('CANCELLED', 'Cancelled'),
)
class Order(models.Model):
    buyer = models.ForeignKey(Account, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='PENDING')
    payment_url = models.CharField(max_length=512, blank=True, null=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    webhook_response = models.JSONField(blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)

    @staticmethod
    def create_order(buyer, address):
        order = Order()
        order.buyer = buyer
        order.address = address
        order.save()
        return order

    def __str__(self):
        return f"Order #{self.id}"
    
    @property
    def total(self):
        return sum([item.total for item in self.order_items.all()])

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='order_items', on_delete=models.CASCADE)
    
    ## for generic reference to product and tickets
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.ticket.price * self.quantity

    @staticmethod
    def create_order_item(order, ticket, quantity):
        order_item = OrderItem()
        order_item.order = order
        order_item.ticket = ticket
        order_item.quantity = quantity
        order_item.save()
        return order_item
