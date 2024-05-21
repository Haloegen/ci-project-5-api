from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductList(generics.ListCreateAPIView):

  serializer_class = ProductSerializer
  permission_classes= [permissions.IsAuthenticatedOrReadOnly]
  queryset = Product.objects.annotate(
    likes_count=Count('likes', distinct=True),
    unlikes_count=Count('unlikes', distinct=True),
    reviews_count=Count('review', distinct=True)
  ).order_by('-created_at')
  filter_backends = [
    filters.OrderingFilter,
    filters.SearchFilter,
    DjangoFilterBackend,
  ]
  filterset_fields = [
    'owner__followed__owner__profile',
    'likes__owner__profile',
    'unlikes__owner__profile',
    'owner__profile',
  ]
  search_fields = [
    'owner__username',
    'title',
  ]
  ordering_fields = [
    'likes_count',
    'unlikes_count',
    'likes__created_at',
    'unlikes__created_at',
  ]

  def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.annotate(
        likes_count=Count('likes', distinct=True),
        unlikes_count=Count('unlikes', distinct=True),
        reviews_count=Count('review', distinct=True),
    ).order_by('-created_at')