from django.contrib import admin

from .models import Order
from .models import OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class BatchFilter(admin.SimpleListFilter) :
    title = 'Batch'
    parameter_name = 'batch'

    def lookups(self,request,model_admin) :
        return (
            ('2020', ('2020')),
            ('2021', ('2021')),
            ('2022', ('2022')),
            ('2023', ('2023')),
        )
    
    def queryset(self,request,queryset) :
        if self.value() :
            year_prefix = self.value()[2:]  # Adjust this if necessary
            return queryset.filter(buyer__email__startswith=year_prefix)
        return queryset

class OrderAdmin(admin.ModelAdmin) :
    list_display = ('buyer', 'buyer_name', 'batch', 'status', 'total')
    search_fields = ('buyer', 'status', 'transaction_id')
    list_filter = ('status', 'created_at', BatchFilter)

    def buyer_name(self, obj):
        return obj.buyer.get_buyer_name()  
    buyer_name.short_description = 'Buyer Name'

    def batch(self, obj) :
        year = obj.buyer.email.split('@')[0][:2]
        
        if year.isnumeric() :
            return int('20' + year)
        
        return 'Unknown'
    batch.short_description = 'Batch'

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
