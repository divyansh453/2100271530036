
from django.urls import path
from .views import ProductAPIView, ProductGETAPIView
urlpatterns = [
    path('categories/<str:categoryname>/products', ProductAPIView.as_view()),
    path('categories/<str:categoryname>/product/<int:productId>', ProductGETAPIView.as_view()),
]