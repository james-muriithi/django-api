from rest_framework import serializers
from .models import News, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['created_at', 'id']
