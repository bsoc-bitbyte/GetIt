from django.contrib import admin
from .models import Product,ProductVariation,ProductColor,ProductSize,ProductImage

# Register your models here.

class ProductAdmin(admin.ModelAdmin) :
    list_display = ("name","seller","type","description","category","tags",'color', 'size', 'price',"created_at","updated_at")
    fields = ("name","seller","type","description","category","tags", "color", "size", "price")

class ProductColorAdmin(admin.ModelAdmin) :
    list_display = ("color",)

class ProductSizeAdmin(admin.ModelAdmin) :
    list_display = ("size",)

class ProductImageAdmin(admin.ModelAdmin) :
    list_display = ("product","image")


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductColor,ProductColorAdmin)
admin.site.register(ProductSize,ProductSizeAdmin)
admin.site.register(ProductImage,ProductImageAdmin)
admin.site.register(ProductVariation)


