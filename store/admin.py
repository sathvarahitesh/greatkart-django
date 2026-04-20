from django.contrib import admin
from .models import Product, Variation

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}

class variationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',) 
    list_filter = ('product', 'variation_category', 'variation_value')
    
admin.site .register(Product, productAdmin)
admin.site.register(Variation, variationAdmin)
    
# class list_display = 
#     admin.ModelAdmin):
#     lasa   t