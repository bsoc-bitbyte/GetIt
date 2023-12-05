from django.db import models

# Create your models here.

category_choices = [
    ('clothing','Clothing'),
    ('rsvp','RSVP'),
]

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600, 
                                   blank=True)
    category = models.CharField(max_length=100, 
                                choices=category_choices)
    primary_variant = models.OneToOneField(
        'ProductVariation', 
        on_delete=models.CASCADE, 
        default=None, 
        null=True,
        blank=True,)
    
    # Need to add Primary Variant and seller Id
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class ProductVariation(models.Model):
    Product = models.ForeignKey(Product, 
                                on_delete=models.CASCADE, 
                                related_name='product_variations')
    ProductColor = models.ForeignKey('ProductColor', 
                                     on_delete=models.CASCADE)
    ProductSize = models.ForeignKey('ProductSize', 
                                    on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    cover_image = models.ForeignKey('ProductImage', 
                                    on_delete=models.CASCADE, 
                                    default=None, null=True,
                                    blank=True,)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.Product.name} {self.ProductColor.color} {self.ProductSize.size}'


class ProductColor(models.Model):
    color = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.color
    
class ProductSize(models.Model):
    size = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.size
    

class ProductImage(models.Model):
    product_variation_id = models.ForeignKey(ProductVariation, 
                                             on_delete=models.CASCADE,
                                             related_name='product_images')
    image = models.ImageField(upload_to='product_images')

    required = ['image']

    def __str__(self):
        return f'{self.product_variation_id.Product.name} {self.product_variation_id.ProductColor.color} {self.product_variation_id.ProductSize.size}'
