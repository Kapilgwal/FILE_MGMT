from rest_framework import serializers
from .models import User, File, FileSeen

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'gender',
            'contact_num',
            'joined_at'
        ]
        read_only_fields = ['id', 'joined_at']


class FileSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()  
    seen_count = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = [
            'id',
            'filename',
            'file',
            'owner',
            'uploaded_at',
            'updated_at',
            'seen_count'
        ]
        read_only_fields = ['id', 'uploaded_at', 'updated_at']

    def get_seen_count(self, obj):
        return obj.seen_by.count()


class FileSeenSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    file = serializers.StringRelatedField()

    class Meta:
        model = FileSeen
        fields = ['id', 'user', 'file', 'seen_at']
        read_only_fields = ['id', 'seen_at']
