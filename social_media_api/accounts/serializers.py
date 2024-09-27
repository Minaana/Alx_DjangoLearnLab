from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Defining the password as a CharField with write_only=True
    password = serializers.CharField(
        max_length=128,  # Add a max length to be explicit about the field size
        write_only=True  # This ensures the password is not included in the API response
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']

    # Override the create method to create a new user
    def create(self, validated_data):
        # Create a new user using the create_user method, which hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Use the password field
            bio=validated_data.get('bio', ''),  # Optional field
            profile_picture=validated_data.get('profile_picture', None)  # Optional field
        )
        return user
