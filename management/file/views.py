# files/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from .serializers import UserSerializer
from accounts.utils import get_user_from_token
from .models import User as LocalUser  # User model in files app


class UserView(APIView):
    """API to fetch or create/update user in files app using token from accounts app"""

    def get_user_from_request(self, request):
        """Extract token from Authorization header and return authenticated user"""
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None
        try:
            token_str = auth_header.split(" ")[1]  # Expect "Token <token>"
        except IndexError:
            return None
        return get_user_from_token(token_str)

    def get(self, request):
        """Return user info from token"""
        user = self.get_user_from_request(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=401)

        return Response({
            "id": user.id,
            "email": user.email,
            "username": user.username,
        })

    def post(self, request):
        """Create or update user in files app using token-authenticated user"""
        user = self.get_user_from_request(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=401)

        try:
            body = json.loads(request.body.decode("utf-8"))
        except Exception:
            return Response({"error": "Invalid JSON"}, status=400)

        first_name = body.get("first_name")
        last_name = body.get("last_name")
        gender = body.get("gender")
        contact_num = body.get("contact_num")

        # Prepare data for serializer
        new_data = {
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender.lower() if gender else None,
            "contact_num": contact_num,
            "email": user.email,
            "username": user.username,
        }

        serializer = UserSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data Feeded Successfully","data" : new_data})
        else:
            return Response(serializer.errors, status=400)
