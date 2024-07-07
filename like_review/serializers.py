from django.db import IntegrityError
from rest_framework import serializers
from like_review.models import LikeReview


class LikeReviewSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikeReview
        fields = ['id', 'created_on', 'owner', 'review']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })