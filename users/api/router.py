from django.urls import path 

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import RegisterView, StudentAPIView, StudyCertificateModelViewSet

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='login-refresh'),
    # path('auth/me'),
    path('register-student', StudentAPIView.as_view(), name='register-student')
]

users_router = DefaultRouter()

users_router.register('study-certificate', StudyCertificateModelViewSet, 'study-certificate')