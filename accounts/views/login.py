from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms import UserLoginForm


def login_view(request):
    form = UserLoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            login(request, form.get_user())
            return redirect("store:store_list")
            
    return render(request, 'accounts/login.html', {"form": form})