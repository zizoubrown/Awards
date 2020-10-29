from rest_framework import serializers
from .models import Profile,Image,Rating

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('user.username','bio')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields=('name','caption','caption')