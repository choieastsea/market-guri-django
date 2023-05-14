from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsOwnerOrReadOnly
# Create your views here.

class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # 인증되지 않은 사용자라면 읽기만 허용

    def perform_create(self, serializer):
        # 생성되기 전, serializer에 user 정보 넣어줘야함
        serializer.save(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True # for partial update
        return super().update(request, *args, **kwargs)
