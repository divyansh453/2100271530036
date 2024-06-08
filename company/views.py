from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Product, Company
from .serializers import ProductSerializer


class ProductAPIViewe(GenericAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    def get(self,request,categoryname):
        
        serializer=self.serializer_class(self.queryset.filter(category=categoryname),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
