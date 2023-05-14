from django.urls import path, include
from question import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'basic', views.QuestionModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]