from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
  "Product model related to the user/owner"
  owner=models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  link = models.URLField(blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  title=models.TextField(blank=True)
  content = models.TextField(blank=True)
  image = models.ImageField(
    upload_to='images/', default='../default_product_rgq6aq', blank=True
  )
  price = models.DecimalField(default=0, decimal_places=2, max_digits=22)

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f'{self.id} {self.title}'