from django.urls import path
from .views import ListProducts

urlpatterns = [
    path('list/', ListProducts.as_view(), name='list-products'),
]