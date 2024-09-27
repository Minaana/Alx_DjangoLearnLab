from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Use CharField for the password with write-only attribute
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']

    # Overriding the create method to handle user creation
    def create(self, validated_data):
        # Use create_user to ensure the password is hashed
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),  # Default to empty if not provided
            profile_picture=validated_data.get('profile_picture', None)  # Optional
        )
        
        # Automatically create a token for the newly created user
        Token.objects.create(user=user)
        return user
