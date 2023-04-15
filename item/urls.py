from django.urls import path, include
from item import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mvs', views.ItemModelViewSet)

urlpatterns = [
    path('', views.index),
    path('create/', views.create_item),
    path('list/', views.ItemListView.as_view()),
    path('detail/<int:pk>/', views.ItemDetailView.as_view()),
    path('list/mixins/', views.ItemListGenericAPIView.as_view()),
    path('detail/mixins/', views.ItemDetailGenericAPIView.as_view()),
    path('list/generics/', views.ItemListGenericView.as_view()),
    path('detail/generics/<int:pk>/', views.ItemDetailGenericView.as_view()),
    path('', include(router.urls))
]