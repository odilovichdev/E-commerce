from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from accounts.utils import get_activation_link
from common.background_job import run_in_background

def send_activation_email(user, request):
    try:
        subject = "Activation your account"
        message = render_to_string(
            "accounts/activation.html",
            {
                "full_name": user.get_fullname,
                "activation_link": get_activation_link(user, request)
            }
        )
        email = EmailMessage(subject, message, to=[user.email])
        email.send()
    except Exception as e:
        raise e



def send_email(request, user):
    link = get_activation_link(user, request)
    subject = "Password reset verification"
    message = f"Passwordni tiklash uchun linkga bosing\n {link}"
    from_email = user.email

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["fazliddinn.gadoyev@gmail.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
    else:
        return HttpResponse("Make sure all fields are entered and valid.")