from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import TemplateView

from ..forms import PasswordResetRequestForm, PasswordResetConfirmForm
from ..models import CustomUser
from ..service import send_email


class SendEmailView(View):
    form_class = PasswordResetRequestForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/send-email.html', {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = CustomUser.objects.get(email=email)
                send_email(request, user)
            except CustomUser.DoesNotExist:
                pass
        return redirect('accounts:email-letter')


class EmailLetterView(TemplateView):
    template_name = 'accounts/email_letter.html'


class PasswordResetCompleteView(View):
    form_class = PasswordResetConfirmForm

    def get(self, request, uuid64, token):
        form = self.form_class()
        return render(request, 'accounts/password-reset.html', {"form": form})

    def post(self, request, uuid64, token):
        form = self.form_class(data=request.POST)
        try:
            uid = urlsafe_base64_decode(uuid64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                messages.success(request, "Password reset successfully!")
                return redirect('accounts:login')
        else:
            return render(request, 'accounts/password-reset.html', {"form": form})
