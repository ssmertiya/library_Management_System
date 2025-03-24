from rest_framework import serializers
from .models import AdminUser, Book
from django.contrib.auth import get_user_model

User = get_user_model() #It return the custom user model.

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #data taken from AdminUser table.
        fields = ['id', 'email', 'password']  # its send all field in API response except password.
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data): #to create admin user at the time of signup
        user = User.objects.create_superuser(**validated_data)
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book       #data taken from Book table.
        fields = '__all__' #its send all fields in API response.
