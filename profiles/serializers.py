from rest_framework import serializers
from profiles import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user.id', 'user.username', 'user.email','user.first_name', 'user.last_name')
