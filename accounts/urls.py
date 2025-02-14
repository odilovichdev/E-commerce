from django.urls import path
from .views import  RegisterView, login_view, logout_view, \
    ActivateEmailView, PasswordResetView, ActivateResetPasswordView
from .views.profile import ProfileView

app_name = 'accounts'

urlpatterns = [
    # auth
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("activate/<uuid64>/<token>/",
         ActivateEmailView.as_view(), name="activate_email"),
    # reset password
    path("reset-password/", PasswordResetView.as_view(), name='reset_password'),
    path("reset-password/<uuid64>/<token>/", ActivateResetPasswordView.as_view(), name="password_reset_confirm"),

    # profile
    path("profile/" ,ProfileView.as_view(), name="profile"),
]
