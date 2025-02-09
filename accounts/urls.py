from django.urls import path
from .views import register_view, RegisterView, login_view, logout_view, \
    ActivateEmailView, SendEmailView, EmailLetterView, PasswordResetCompleteView

app_name = 'accounts'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("activate/<uuid64>/<token>/",
         ActivateEmailView.as_view(), name="activate_email"),
    path("send-email/" ,SendEmailView.as_view(), name="send-email"),
    path("email-letter/", EmailLetterView.as_view(), name='email-letter'),
    path("password-reset/<uuid64>/<token>/", PasswordResetCompleteView.as_view(), name="password-reset"),
]
