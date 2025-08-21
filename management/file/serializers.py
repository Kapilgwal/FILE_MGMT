from rest_framework import serializers
from .models import User, File, FileSeen


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model (id is read-only)."""

    class Meta:
        model = User
        fields = [
            "id",          # always returned in responses
            "username",
            "email",
            "first_name",
            "last_name",
            "gender",
            "contact_num",
            "joined_at",
        ]
        read_only_fields = ["id", "joined_at"]  # won't be required in input


class FileSerializer(serializers.ModelSerializer):
    """Serializer for File model."""
    owner = serializers.StringRelatedField(read_only=True)  
    seen_count = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = [
            "id",
            "filename",
            "file",
            "owner",
            "uploaded_at",
            "updated_at",
            "seen_count",
        ]
        read_only_fields = ["id", "uploaded_at", "updated_at"]

    def get_seen_count(self, obj):
        return obj.seen_by.count()


class FileSeenSerializer(serializers.ModelSerializer):
    """Serializer for FileSeen model."""
    user = serializers.StringRelatedField(read_only=True)
    file = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FileSeen
        fields = ["id", "user", "file", "seen_at"]
        read_only_fields = ["id", "seen_at"]
