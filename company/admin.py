from django.contrib import admin
from .models import Company,Product,Category
# Register your models here.
admin.site.register(Company)
admin.site.register(Category)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('productName','price','rating','discount','availability','company'),
        }),
    )