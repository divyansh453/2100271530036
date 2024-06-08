from rest_framework import serializers
from .models import Company, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['productName','price','rating','discount','availability']
