# views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer


class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Atau permissions lain yang sesuai

    def get_queryset(self):
        """
        Opsi tambahan untuk filter, misalnya berdasarkan kategori, bisa ditambahkan di sini.
        """
        return super().get_queryset()
