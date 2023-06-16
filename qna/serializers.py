from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only= True)
    class Meta:
        model = Question
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        username = data['user']
        # 가운데 문자 가리기
        masked_username = username[:2] + '*' * (len(username)-4) + username[-2:]
        data['user'] = masked_username
        return data

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True) # question 내용도 보여주기
    class Meta:
        model = Answer
        fields = "__all__"
