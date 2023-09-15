from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    id = serializers.IntegerField()


    class Meta:
        model = Favorite
        fields = ('id', 'product')
