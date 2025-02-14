from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.shortcuts import render, redirect

from ..forms import PasswordResetForm, ActivateResetPasswordForm
from ..models import CustomUser
from ..service import send_reset_password_email


class PasswordResetView(View):
    form_class = PasswordResetForm
    template_name = "accounts/forget_password.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = CustomUser.objects.get(email=email)
            send_reset_password_email(user, request)
            messages.success(request, "Password reset link email send successfully")
            return redirect("accounts:login")
        return render(request, self.template_name, {"form": form})


class ActivateResetPasswordView(View):
    def get(self, request, uuid64, token):
        try:
            uid = urlsafe_base64_decode(uuid64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            request.session['uid'] = uid
            form = ActivateResetPasswordForm()
            context = {
                "form": form
            }
            messages.success(request, "Please enter your new password")
            return render(request, 'accounts/activate_reset_password.html', context)
        else:
            messages.error(request, "Reset password link is invalid.")
            return redirect('accounts:login')

    def post(self, request, uuid64, token):
        try:
            uid = request.session.get("uid")
            user = CustomUser.objects.get(pk=uid)
        except CustomUser.DoesNotExist:
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            form = ActivateResetPasswordForm(data=request.POST)
            if form.is_valid():
                password = form.cleaned_data.get("password")
                user.set_password(password)
                user.save()
                messages.success(request, "Password reset successfully.")
                return redirect("accounts:login")
            context = {
                "form": form
            }
            return render(request, 'accounts/activate_reset_password.html', context)
        messages.error(request, "Reset password link is invalid")
        return redirect("accounts:login")













