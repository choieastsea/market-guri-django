from rest_framework import serializers
from .models import Profile
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class LoginSerializer(serializers.Serializer):
    """
    로그인 시, 입력을 검증하기 위한 serializer
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if len(username) > 0 or len(password) > 0:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise AuthenticationFailed('비활성화된 사용자입니다')
            else:
                raise AuthenticationFailed('아이디나 비밀번호가 다릅니다')
        else:
            raise AuthenticationFailed('아이디와 비밀번호 모두 입력해야합니다')

        return data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
    def create(self, validated_data):
        """
        회원 가입시, 비밀번호 암호화 처리를 추가
        """
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        user = Profile.objects.create(**validated_data)
        return user