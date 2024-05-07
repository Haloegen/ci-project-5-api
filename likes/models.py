from django.db import models
from django.contrib.auth.models import User
from products.models import Product



class Like(models.Model):
    """
    like model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'product']

    def __str__(self):
        return f"{self.owner} ,{self.product}"