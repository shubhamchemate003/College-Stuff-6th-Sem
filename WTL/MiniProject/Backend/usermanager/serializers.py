from rest_framework import fields, serializers

from usermanager.models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'email','category')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'password','category', 'address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],category=validated_data['category'], address=validated_data['address'])
        user.set_password(validated_data['password'])
        user.save()
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")