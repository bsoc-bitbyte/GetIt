from rest_framework.serializers import ModelSerializer

from .models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id',
                  'product',
                  'buyer',
                  'quantity',
                  'total',
                  'created_at',
                  'updated_at')
        kwargs = {
            'buyer': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'total': {'read_only': True}
        }

    # in the create method, we will override the create method to add the buyer to the order and calculate the total
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.save()
        return order
