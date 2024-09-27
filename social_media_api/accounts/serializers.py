from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # Import Token model for authentication tokens

# Get the custom or default user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Ensure the password is write-only and secured with CharField
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']

    # Override the create method to create a new user
    def create(self, validated_data):
        # Use create_user to hash the password and create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Password is passed and hashed
            bio=validated_data.get('bio', ''),  # Optional bio
            profile_picture=validated_data.get('profile_picture', None)  # Optional profile picture
        )
        
        # Create an authentication token for the user
        Token.objects.create(user=user)
        
        return user

