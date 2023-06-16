from django.urls import path, include
from qna import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'question', views.QuestionModelViewSet)
router.register(r'answer', views.AnswerModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]