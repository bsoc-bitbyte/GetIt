from django.utils.html import escape
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from markdown_it import MarkdownIt
from .models import Product, ProductImage, ProductVariation, ProductColor, ProductSize

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

class ProductVariationSerializer(ModelSerializer):
    color = serializers.CharField(source='ProductColor.color', read_only=True)
    size = serializers.CharField(source='ProductSize.size', read_only=True)
    
    class Meta:
        model = ProductVariation
        fields = ('id', 'color', 'size', 'price', 'quantity', 'is_active')

class ProductSerializer(ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    variations = ProductVariationSerializer(source='product_variations', many=True, read_only=True)  # Just add this line
    
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'seller',
            'type',
            'description',
            'category',
            'tags',
            'price',
            'color',
            'size',
            'created_at',
            'updated_at',
            'product_images',
            'variations',
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