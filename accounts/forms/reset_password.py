from django.core.exceptions import ValidationError
from django import forms
from ..models import CustomUser



class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Send email")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Bu email ro'yxatdan o'tmagan!")
        return email


class ActivateResetPasswordForm(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean(self):
        data = super().clean()
        password2 = data.pop("password2")
        password = data.get("password")


        if password and password2 and password2 != password:
            raise ValidationError("Ikkita password bir xil bo'lishi kerak!")

        if len(password)<4:
            raise ValidationError("Password uzunligi 4 ta dan kam bo'lmasligi kerak!")

        return data
