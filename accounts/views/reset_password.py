from django.views import View
from django.shortcuts import render, redirect

from ..forms import PasswordResetForm
from ..models import CustomUser


class PasswordResetView(View):
    form_class = PasswordResetForm

    def get(self, request):
        form = self.form_class()
        return render(request, "accounts/forget_password.html", {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = CustomUser.objects.get(email=email)

