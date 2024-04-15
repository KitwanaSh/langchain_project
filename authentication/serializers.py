from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=25)
    password = serializers.CharField(write_only=True, required=True)


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user