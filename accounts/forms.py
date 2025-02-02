from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django import forms
from .models import CustomUser


# class CustomUserCreationForm(forms.Form):

#     email = forms.EmailField(label="Email", max_length=255, required=True)
#     first_name = forms.CharField(label="Enter your first name", max_length=255)
#     last_name = forms.CharField(label="Enter your last name", max_length=255)
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label="Confirm Password", widget=forms.PasswordInput)

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if "@" not in email:
#             raise ValidationError("Email xato kiritilgan!")

#         if CustomUser.objects.filter(email=email).exists():
#             raise ValidationError("Bu email bilan ro'yxatdan o'tilgan")

#         return email

#     def clean_password(self):
#         password = self.cleaned_data['password']
#         if len(password) < 4:
#             raise ValidationError(
#                 "Password uzunligi 4 tadan katta bo'lishi kerak!")
#         return password

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password2 = cleaned_data.get('password2')

#         if password and password2 and password2 != password:
#             raise ValidationError("Parollar bir xil bo'lishi kerak")
#         return cleaned_data

#     def save(self, commit=True):
#         user = CustomUser.objects.create_user(
#             email=self.cleaned_data.get("email"),
#             first_name=self.cleaned_data.get("first_name"),
#             last_name=self.cleaned_data.get("last_name"),
#             password=self.cleaned_data.get("password")
#         )
#         return user


class CustomUserCreationForm(forms.ModelForm):
    password2 = forms.CharField(label="Confirm Password", 
        widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        )
        labels = {
            "email": "Email",
            "first_name": "Enter your first name",
            "last_name": "Enter your last name",
            "password": "Password"
        }
        widgets = {
            "password": forms.PasswordInput
        }
    
    def clean_email(self):
        email = self.cleaned_data['email']

        if "@" not in email:
            raise ValidationError("Email xato kiritildi!")
        
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Bu email bilan user ro'yxatdan o'tgan!")
        
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.pop("password2")
        

        if password and password2 and password2!=password:
            raise ValidationError("Parollar bir xil bo'lishi kerak")
        

        if password and len(password)<4:
            raise ValidationError("Parol 4 tadan kam bo'lmasligi keark")

        return cleaned_data
    
    def save(self):
        user = CustomUser.objects.create_user(
            **self.cleaned_data
        )
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Enter your password",
        widget=forms.PasswordInput)
    user = None
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise ValidationError("Email yoki password xato!")
            
            if not self.user.is_active:
                raise ValidationError("User active emas!")
        
        return cleaned_data
    
    def get_user(self):
        return self.user
        