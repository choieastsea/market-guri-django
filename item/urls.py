from django.urls import path, include
from item import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'basic', views.ItemModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]