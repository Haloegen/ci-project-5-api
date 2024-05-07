from django.db import IntegrityError
from rest_framework import serializers
from .models import Unlike

class UnlikeSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = Unlike
    fields = ['id', 'created_at', 'owner', 'product']

  def create(self, validated_data):
    try:
      return super().create(validated_data)
    except IntegrityError:
      raise serializers.ValidationError({
      'detail': 'possible duplicate'
      })