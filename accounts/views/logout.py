from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="accounts:login")
def logout_view(request):
    logout(request)
    return redirect("accounts:login")
