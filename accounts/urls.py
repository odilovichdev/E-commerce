from django.urls import path
from .views import register_view, RegisterView, login_view, logout_view, \
    ActivateEmailView

app_name = 'accounts'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("activate/<uuid64>/<token>/",
         ActivateEmailView.as_view(), name="activate_email"),
]
