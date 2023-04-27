from rest_framework import serializers
from .models import Profile
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    """
    로그인 시, 입력을 검증하기 위한 serializer
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if len(username) > 0 and len(password) > 0:
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
    
class UserInfoSerializer(serializers.ModelSerializer):
    """
    user에 대하여 해당 사용자의 username과 profile 정보를 보여주는 serializer
    """
    profile = ProfileSerializer()   #one to one field이므로, user에 해당하는 profile을 가져오면 됨
    class Meta:
        model = User
        fields = ('username', 'profile')
        