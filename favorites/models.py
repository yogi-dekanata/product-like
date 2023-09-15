from django.db import models
from products.models import Product
from users.models import CustomUser


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'favorites'
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_favorite')
        ]
