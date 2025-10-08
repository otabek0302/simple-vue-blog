from django.urls import path
from .views import RegistrationViewSet, LoginView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path("register/", RegistrationViewSet.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
]