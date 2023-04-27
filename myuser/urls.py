from django.urls import path
from myuser import views

urlpatterns = [
    path('login/', views.login_view)
]