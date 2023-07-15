from django.contrib import admin
from .models import Product,ProductVariation,ProductColor,ProductSize,ProductImage

# Register your models here.

class ProductAdmin(admin.ModelAdmin) :
    list_display = ("name","description","category","created_at","updated_at")

class ProductVariationAdmin(admin.ModelAdmin) :
    list_display = ("product_id","color_id","size_id","price","quantity")

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



