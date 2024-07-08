from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from like_review.models import LikeReview
from like_review.serializers import LikeReviewSerializer

class LikeReviewList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeReviewSerializer
    queryset = LikeReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeReviewDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeReviewSerializer
    queryset = LikeReview.objects.all()