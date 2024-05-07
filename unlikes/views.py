from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Unlike
from .serializers import UnlikeSerializer


class UnlikeList(generics.ListCreateAPIView):
  serializer_class= UnlikeSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Unlike.objects.all()

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class UnlikeDetail(generics.RetrieveDestroyAPIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = UnlikeSerializer
  queryset = Unlike.objects.all()