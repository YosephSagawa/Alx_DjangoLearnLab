from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['id', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'bio']


    def create(self, validated_data):
        # Use create_user() instead of manually setting password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            bio=validated_data.get('bio', '')
        )

        # Create a token for the new user
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        Token = Token.objects.create()
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data['user'] = user
        return data