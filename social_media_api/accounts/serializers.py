from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # Import Token model for authentication tokens

# Get the user model (custom or default user model)
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Use CharField for the password with write-only attribute
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']

    # Overriding the create method to handle user creation
    def create(self, validated_data):
        # Extract the password from validated data
        password = validated_data.pop('password')
        
        # Use create_user to ensure the password is hashed and other fields are properly set
        user = User.objects.create_user(
            username=validated_data['username'],
            bio=validated_data.get('bio', ''),  # Optional field
            profile_picture=validated_data.get('profile_picture', None)  # Optional field
        )
        
        # Set the user's password (hashed internally)
        user.set_password(password)
        
        # Save the user instance
        user.save()

        # Automatically create a token for the newly created user
        Token.objects.create(user=user)
        
        return user
