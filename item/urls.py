from django.urls import path
from item import views
urlpatterns = [
    path('', views.index),
    path('create/', views.create_item),
    path('list/', views.ItemListView.as_view()),
    path('detail/<int:pk>/', views.ItemDetailView.as_view())
]