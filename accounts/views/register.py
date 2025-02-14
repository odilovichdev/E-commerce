from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from ..models import CustomUser
from ..forms import CustomUserCreationForm
from ..service.activation_email import send_activation_email


class RegisterView(CreateView):
    model = CustomUser
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")


    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        send_activation_email(user, self.request)
        messages.success(
            self.request, "Muvaffaqiyatli ro'yxatdan o'tdingiz! "
                          "Accauntingizni faollashtirish uchun emailingizga link yuborildi")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Iltimos formani to'g'ri to'ldiring!")
        return super().form_invalid(form)


# class RegisterView(View):
#     model = CustomUser
#     form_class = CustomUserCreationForm
#     template_name = 'accounts/register.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {"form":form})


#     def post(self, request, *args, **kwargs):
#         form = self.form_class(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, "Muvaffaqiyatli ro'yxatdan o'tdingiz! Endi tizimga kiring.")
#             return redirect("store:store_list")
#         return render(request, self.template_name, {"form": form})

# def register_view(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, "Muvaffaqiyatli ro'yxatdan o'tdingiz! Endi tizimga kiring.")
#             return redirect("store:store_list")
#         else:
#             return render(request, 'accounts/register.html', {"form": form})
#     else:
#         form = CustomUserCreationForm()
#         return render(request, 'accounts/register.html', {"form": form})
