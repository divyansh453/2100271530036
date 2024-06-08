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
        n=int(request.GET.get('n'))
        query=self.queryset.filter(category=categoryname)[:n]
        page_number=1
        p = Paginator(query,10)
        pages=p.num_pages
        count=query.count()
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        serializer=self.serializer_class(page_obj,many=True)
        response={"no_of_pages":pages,"no_of_products":count,"blogs":serializer.data}
        
        return Response(response,status=status.HTTP_200_OK)
