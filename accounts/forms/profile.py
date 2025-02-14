from django import forms
from ..models.profile import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user", "created_at", "updated_at", "is_active"]
