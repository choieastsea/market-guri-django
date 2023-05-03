from django.contrib.auth.signals import user_logged_in
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from .models import UserSession

@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    # 해당 사용자의 기존 세션 삭제
    Session.objects.filter(usersession__user=user).delete()
    
    # 현재 요청에 대한 새로운 세션 저장
    request.session.save()

    # UserSession 테이블에도 새롭게 생성
    UserSession.objects.get_or_create(
        user=user,
        session_id=request.session.session_key
    )
