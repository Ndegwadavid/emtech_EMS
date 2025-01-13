
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AdminSignupView, AdminSigninView

urlpatterns = [
    path('signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('signin/', AdminSigninView.as_view(), name='admin-signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]