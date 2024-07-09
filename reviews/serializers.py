from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review
from like_review.models import LikeReview  # Ensure this import is present

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_review_id = serializers.SerializerMethodField()
    like_review_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_review_id(self, obj): 
        user = self.context['request'].user
        if user.is_authenticated:
            like = LikeReview.objects.filter(
                owner=user, review=obj
            ).first()
            return like.id if like else None
        return None

    def get_like_review_count(self, obj):
        return obj.review_likes.count()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'product', 
            'like_review_id', 'like_review_count', 'created_at', 'updated_at', 'content'
        ]

class ReviewDetailSerializer(ReviewSerializer):
    product = serializers.ReadOnlyField(source="product.id")
