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
