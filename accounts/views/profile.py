from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import ProfileForm
from accounts.models import Profile


class ProfileView(View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile)
        context = {
            "form": form,
            "instance": profile
        }
        return render(request, "accounts/profile.html", context)

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(data=request.POST, instance=profile, files=request.FILES)
        context = {
            "form": form,
            "instance": profile
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated is successfully")
            return redirect("accounts:profile")
        return render(request, 'accounts/profile.html',context)

