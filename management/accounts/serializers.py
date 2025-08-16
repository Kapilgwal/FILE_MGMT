from rest_framework import serializers
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","username")

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,min_length = 6)

    class Meta:
        model = User 
        fields = ("email","username","password")

    def create(self,validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return User 
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

