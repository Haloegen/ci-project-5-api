from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
  serializer_class= ProfileSerializer
  queryset = Profile.objects.annotate(
    products_count=Count('owner__product', distinct=True),
    followers_count = Count('owner__followed', distinct= True),
    following_count = Count('owner__following', distinct= True)
  ).order_by('-created_at')
  filter_backends = [
    filters.OrderingFilter,
    DjangoFilterBackend,
  ]
  filterset_fields = [
    'owner__following__followed__profile',
    'owner__followed__owner__profile',



  ]
  ordering_fields = [
    'products_count',
    'followers_count',
    'following_count',
    'owner__following__created_at',
    'owner_followed_created_at'
  ]
    


class ProfileDetail(generics.RetrieveUpdateAPIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = ProfileSerializer
  queryset = Profile.objects.annotate(
    products_count=Count('owner__product', distinct=True),
    followers_count = Count('owner__followed', distinct= True),
    following_count = Count('owner__following', distinct= True)
  ).order_by('-created_at')