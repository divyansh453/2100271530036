
from django.urls import path
from .views import ProductAPIViewe
urlpatterns = [

    path('products/', ProductAPIViewe.as_view()),
    path('categories/<str:categoryname>/product', ProductAPIViewe.as_view()),
]