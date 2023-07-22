from django.contrib import admin
from .models import Product,ProductVariation,ProductColor,ProductSize,ProductImage

# Register your models here.

class ProductAdmin(admin.ModelAdmin) :
    list_display = ("name","description","category",'primary_variant',"created_at","updated_at")
    fields = ("name","description","category","primary_variant",)

class ProductVariationAdmin(admin.ModelAdmin) :
    list_display = ("Product","ProductSize","ProductColor","price","quantity")

class ProductColorAdmin(admin.ModelAdmin) :
    list_display = ("color",)

class ProductSizeAdmin(admin.ModelAdmin) :
    list_display = ("size",)

class ProductImageAdmin(admin.ModelAdmin) :
    list_display = ("product_variation_id","image")


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductVariation,ProductVariationAdmin)
admin.site.register(ProductColor,ProductColorAdmin)
admin.site.register(ProductSize,ProductSizeAdmin)
admin.site.register(ProductImage,ProductImageAdmin)



