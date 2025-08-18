from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.views import APIView 

from .models import User, Token 
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer


def home(request):
    return JsonResponse({
        'msg': 'Hello, this is accounts package which will handle the login, logout and register details'
    })


# Helper to fetch user from token
def get_user_from_token(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Token "):  
        return None 
    
    key = auth_header.split(" ")[1]

    try:
        token = Token.objects.get(key=key)
        if token.is_expired():
            token.delete()
            return None 
        return token.user 
    except Token.DoesNotExist:
        return None
    

# Register
class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]


# Login
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=400)
        
        if not user.check_password(password):
            return Response({"detail": "Invalid credentials"}, status=400)

        # Generate a token
        token = Token.generate(user)

        return Response({
            "user": UserSerializer(user).data,
            "token": token.key,
            "expires_at": token.expires_at,
        }, status=status.HTTP_200_OK)


# Logout
class LogoutView(APIView):
    def post(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Token "):
            return Response({"detail": "Token required"}, status=400)

        key = auth_header.split(" ")[1]        
        Token.objects.filter(key=key).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Me (get current user)
class MeView(APIView):
    def get(self, request):
        user = get_user_from_token(request)
        if not user:
            return Response({"detail": "Not authenticated"}, status=401)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
