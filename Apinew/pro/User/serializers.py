from rest_framework import serializers
from .models import ApiModel

class APiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = ('id','name','surname','age')