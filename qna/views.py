from rest_framework import viewsets
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsOwnerOrReadOnly
# Create your views here.

class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # 인증되지 않은 사용자라면 읽기만 허용

    def perform_create(self, serializer):
        # question 생성되기 전, serializer에 auth에 해당하는 user 정보 넣어줘야함
        serializer.save(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True # for partial update
        return super().update(request, *args, **kwargs)

class AnswerModelViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    allowed_methods = ['GET'] # only for get (답변은 관리자페이지에서 작성하므로, 사용자에게 보여주기만 하면 됨)
    def get_queryset(self):
        # 특정 item_code에 대한 QNA 보여주도록 /qna/answer/?item_code=2
        queryset = Answer.objects.all()
        item_id = self.request.query_params.get('item_code')
        if item_id is not None:
            queryset = queryset.filter(question__item=item_id)
        return queryset