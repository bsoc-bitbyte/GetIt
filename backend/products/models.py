from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600, blank=True)
    category = models.CharField(max_length=100)
    primary_variant = models.OneToOneField(
        'ProductVariation', on_delete=models.CASCADE, default=None, null=True)
    
    # Need to add Primary Variant and seller Id
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class ProductVariation(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    color_id = models.ForeignKey('ProductColor', on_delete=models.CASCADE)
    size_id = models.ForeignKey('ProductSize', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    cover_image = models.ForeignKey('ProductImage', on_delete=models.CASCADE, default=None, null=True)
    is_active = models.BooleanField(default=True)

    required = ['product_id', 'color_id', 'size_id', 'price', 'quantity']

    def __str__(self):
        return f'{self.product_id.name} {self.color_id.color} {self.size_id.size}'


class ProductColor(models.Model):
    color = models.CharField(max_length=100, unique=True)

    required = ['color']

    def __str__(self):
        return self.color
    
class ProductSize(models.Model):
    size = models.CharField(max_length=100, unique=True)

    required = ['size']

    def __str__(self):
        return self.size
    

class ProductImage(models.Model):
    product_variation_id = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    required = ['image']

    def __str__(self):
        return f'{self.product_variation_id.product_id.name} {self.product_variation_id.color_id.color} {self.product_variation_id.size_id.size}'
