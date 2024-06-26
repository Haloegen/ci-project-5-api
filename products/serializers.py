
from rest_framework import serializers
from .models import Product
from likes.models import Like
from unlikes.models import Unlike

class ProductSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  is_owner = serializers.SerializerMethodField()
  profile_id=serializers.ReadOnlyField(source='owner.profile.id')
  profile_image=serializers.ReadOnlyField(source='owner.profile.image.url')
  like_id = serializers.SerializerMethodField()
  unlike_id = serializers.SerializerMethodField()
  reviews_count = serializers.ReadOnlyField()
  likes_count = serializers.ReadOnlyField()
  unlikes_count = serializers.ReadOnlyField()



  def validate_image(self, value):
      if value.size > 1024 * 1024 * 2:
        raise serializers.ValidationError(
          "Image size larger than 2mb"
        )
      if value.image.width > 4096:
        raise serializers.ValidationError(
          'Image width larger than 4096px'
        )
        
      if value.image.height > 4096:
        raise serializers.ValidationError(
          "Image height larger than 4096px"
        )
      return value
      
  def get_is_owner(self, obj):
    request = self.context['request']
    return request.user == obj.owner


  def get_like_id(self, obj):
    user = self.context['request'].user
    if user.is_authenticated:
      like = Like.objects.filter(
        owner = user, product = obj
      ).first()
      return like.id if like else None
    return None
  
  def get_unlike_id(self, obj):
    user = self.context['request'].user
    if user.is_authenticated:
      unlike = Unlike.objects.filter(
        owner = user, product = obj
      ).first()
      return unlike.id if unlike else None
    return None


  class Meta:
    model = Product
    fields = [
    'id', 'owner', 'link', 'is_owner', 'profile_id', 'profile_image', 'created_at', 'updated_at', 'title',
    'content','price', 'image', 'like_id', 'unlike_id', 'reviews_count', 'likes_count', 'unlikes_count'
    ]
