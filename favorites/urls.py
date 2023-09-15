# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('like-product/', views.ProductLike.as_view(), name='like-product'),
    path('liked/', views.RetrieveLikedProducts.as_view(), name='retrieve-liked-products'),
    path('cancel-product/', views.CancelProductLike.as_view(), name='cancel-like-product'),
]
