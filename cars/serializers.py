from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Car
        fields = ('id', 'make', 'model', 'description', 'imgUrl', 'price', 'year')

# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     make = serializers.CharField(required=False, allow_blank=True)
#     description = serializers.CharField(max_length=255, required=False, allow_blank=True)
#     imgUrl = serializers.CharField(max_length=255, required=False, allow_blank=True)
#     price = serializers.IntegerField(required=False)
#     year = serializers.IntegerField(required=False)

