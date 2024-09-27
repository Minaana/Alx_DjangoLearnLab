from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get the custom user model
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
        
        # Create a new user instance using the create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            bio=validated_data.get('bio', ''),  # Optional field
            profile_picture=validated_data.get('profile_picture', None)  # Optional field
        )
        
        # Set the password (ensure it's hashed)
        user.set_password(password)
        
        # Save the user
        user.save()
        
        return user
