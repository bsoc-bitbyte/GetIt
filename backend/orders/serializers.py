from rest_framework.serializers import ModelSerializer, SerializerMethodField

from tickets.serializers import TicketSerializer

from .models import Order, OrderItem


class OrderItemmSerializer(ModelSerializer):
    ticket = TicketSerializer(read_only = True)
    class Meta:
        model = OrderItem
        fields = ('id',
                  'ticket',
                  'quantity',
                  )
        kwargs = {
            'order': {'read_only': True},
        }

class OrderSerializer(ModelSerializer):
    
    order_items = OrderItemmSerializer(many = True, read_only = True)
    order_name = SerializerMethodField()
    buyer = SerializerMethodField()
    buyer_name = SerializerMethodField()
    class Meta:
        model = Order
        
        fields = ('id',
                  'buyer',
                  'buyer_name',
                  'address',
                  'total',
                  'transaction_id',
                  'payment_url',
                  'status',
                  'order_name',
                  'order_items',
                  'payment_url',
                  'created_at',
                  'updated_at')
        kwargs = {
            'buyer': {'read_only': True},
            'buyer_name': {'read_only': True},
            'total': {'read_only': True},
            'payment_url': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }

    def get_order_name(self, obj):
        if obj.order_items.exists():
            order_name = obj.order_items.first().ticket.event.title
            additional_items = obj.order_items.count() - 1
            if additional_items > 0:
                order_name += f" + {additional_items}"
            return order_name
        return ""
    
    def get_buyer(self, obj):
        return obj.buyer.email
    
    def get_buyer_name(self, obj):
        return obj.buyer.first_name + " " + obj.buyer.last_name

    # in the create method, we will override the create method to add the buyer to the order and calculate the total
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.save()
        return order
