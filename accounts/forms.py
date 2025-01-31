from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255)
    first_name = forms.CharField(label="Enter your first name", max_length=255)
    last_name = forms.CharField(label="Enter your last name", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if "@" not in email:
            raise ValidationError("Email xato kiritilgan!")

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Bu email bilan ro'yxatdan o'tilgan")

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise ValidationError(
                "Password uzunligi 4 tadan katta bo'lishi kerak!")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password2 != password:
            raise ValidationError("Parollar bir xil bo'lishi kerak")
        return cleaned_data

    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            email=self.cleaned_data.get("email"),
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            password=self.cleaned_data.get("password")
        )
        return user
