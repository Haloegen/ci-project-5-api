from rest_framework import generics, permissions, filters
from drf_API.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer

class ReviewList(generics.ListCreateAPIView):
  serializer_class= ReviewSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Review.objects.all()
  filter_backends = [
    DjangoFilterBackend,
  ]
  filterset_fields = [
    'product'
  ]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = ReviewDetailSerializer
  queryset = Review.objects.all()

  
  