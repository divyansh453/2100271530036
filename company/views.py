from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(GenericAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    def get(self,request,categoryname):
        n=int(request.GET.get('n'))

        query=self.queryset.filter(category=categoryname)
        rating=request.GET.get('rating')
        if rating:
            query=query.filter(rating__gte=rating)
        price=request.GET.get('price')
        if price:
            query=query.filter(price__gte=price)
        company=request.GET.get('company')
        if company:
            query=query.filter(company__code= company)
        discount=request.GET.get('discount')
        if discount:
            query=query.filter(discount__gte=discount)
        page_number=1
        query=query[:n]
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


class ProductGETAPIView(GenericAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    def get(self,request,categoryname,productId):

        query=get_object_or_404(Product , id=productId,category=categoryname)

        serializer=self.serializer_class(query,many=False)
        response={"status":200,"data":serializer.data}
        
        return Response(response,status=status.HTTP_200_OK)
