from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

# 패스워드가 필요없는 다른 테이블에서 사용할 용도
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'