from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, DestroyAPIView, get_object_or_404

from .models import Favorite, Product
from .serializers import FavoriteSerializer


class RetrieveLikedProducts(generics.ListAPIView):
    """
    API View for retrieving all products that a user has liked.
    """
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class ProductLike(CreateAPIView):
    """
    API View for liking a specific product.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        product = self.get_product_from_request()
        if Favorite.objects.filter(user=self.request.user, product=product).exists():
            return self.respond_already_liked()

        favorite = Favorite.objects.create(user=self.request.user, product=product)
        serializer = FavoriteSerializer(favorite)

        return Response({"success": "Product liked", "favorite": serializer.data}, status=status.HTTP_201_CREATED)

    def get_product_from_request(self):
        product_id = self.request.data.get('id')
        return get_object_or_404(Product, id=product_id)

    def respond_already_liked(self):
        return Response({"error": "Already liked this product"}, status=status.HTTP_400_BAD_REQUEST)


class CancelProductLike(DestroyAPIView):
    """
    API View to cancel a 'like' for a specific product.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        """
        Remove the 'like' relationship between the user and a product, if it exists.
        """
        product_id = request.data.get('id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            favorite = Favorite.objects.get(user=self.request.user, product=product)
            favorite.delete()
            return Response({"success": "Product unliked"}, status=status.HTTP_200_OK)
        except Favorite.DoesNotExist:
            return Response({"error": "You have not liked this product yet"}, status=status.HTTP_400_BAD_REQUEST)
