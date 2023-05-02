from django.urls import path
from myuser import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('session/', views.session_view),
    path('signup/', views.signup_view),
]