from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from accounts.utils import get_activation_link
from common.background_job import run_in_background


def send_password_reset_email(user, request):
    try:
        subject = "Password reset link"
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
