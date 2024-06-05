from django.utils.html import escape
from rest_framework.serializers import ModelSerializer
from markdown_it import MarkdownIt
from .models import Product, ProductImage

md = (
    MarkdownIt('commonmark' ,{'html':False})
    .enable('table')
)

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
        )

class ProductSerializer(ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'color',
            'size',
            'created_at',
            'updated_at',
            'product_images',
        )

    def validate_name(self, value):
        return escape(value)
    
    def validate_description(self, value):
        return md.render(value)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        filtered_images = instance.product_images.filter(product=instance)
        representation['product_images'] = ProductImageSerializer(filtered_images, many=True).data
        return representation
