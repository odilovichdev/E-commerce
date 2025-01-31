from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# class RegisterView(CreateView):
#     model = CustomUser
#     template_name = "accounts/register.html"
#     form_class = UserCreationForm


def register_view(request):

    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz! Endi tizimga kiring.")
            return redirect("store:store_list")
        else:
            return render(request, 'accounts/register.html', {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {"form": form})
