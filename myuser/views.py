from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, ProfileSerializer
from django.contrib.auth import login, logout
from rest_framework import status

@api_view(['GET'])
def session_view(request):
    """
    사용자의 인증 여부를 반환하는 함수
    """
    return Response({"detail" : request.user.is_authenticated}, status=status.HTTP_200_OK)

@api_view(['POST'])
def login_view(request):
    """
    세션 방식으로 로그인을 처리하는 함수
    """
    login_serailizer = LoginSerializer(data=request.data)
    if login_serailizer.is_valid():
        # 유효한 입력의 경우 로그인
        user = login_serailizer.validated_data['user']
        user_info = ProfileSerializer(user)
        login(request,user)
        return Response({"detail" : user_info.data},status=status.HTTP_202_ACCEPTED)
    else:
        return Response(login_serailizer.errors)

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response({"detail" : request.user.is_authenticated}, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup_view(request):
    """
    회원가입을 처리하는 함수
    """
    print(request.data)
    profile_serializer = ProfileSerializer(data=request.data)
    if profile_serializer.is_valid():
        # 유효한 입력의 경우 회원가입 완료
        profile_serializer.save() # create 호출
        return Response({"detail" : 'signup success'},status=status.HTTP_201_CREATED)
    else:
        return Response(profile_serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
