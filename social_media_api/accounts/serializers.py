from rest_framework import serializers
from django.contrib.auth import get_user_model  # To get the custom or default user model
from rest_framework.authtoken.models import Token  # To generate tokens

# Get the custom or default user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Explicitly define the password as a CharField with write_only=True
    password = serializers.CharField(
        max_length=128,
        write_only=True  # Ensure password is write-only and not exposed in responses
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user using the get_user_model().objects.create_user() method
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Password is hashed by create_user
            bio=validated_data.get('bio', ''),  # Optional field
            profile_picture=validated_data.get('profile_picture', None)  # Optional field
        )
        
        # Create a token for the newly created user
        Token.objects.create(user=user)
        
        return user
    
    from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # Import Token model for token creation

# Get the user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Define the password as a CharField with write_only=True
    password = serializers.CharField(
        max_length=128,
        write_only=True  # Ensure password is not included in the API response
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user using the create_user method, which automatically hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Password is hashed
            bio=validated_data.get('bio', ''),  # Optional field
            profile_picture=validated_data.get('profile_picture', None)  # Optional field
        )
        
        # Create an authentication token for the user
        Token.objects.create(user=user)
        
        return user

