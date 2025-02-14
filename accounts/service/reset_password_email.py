"""
Send reset password email to user
"""
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from accounts.utils import get_link
from common.background_job import run_in_background



@run_in_background
def send_reset_password_email(user, request):
    try:
        subject = "Reset your password"
        message = render_to_string(
            "accounts/reset_password.html",
            {
                "full_name": user.get_fullname,
                "password_reset_link": get_link(user, request, redirect_url="reset-password")
            }
        )
        email = EmailMessage(subject, message, to=[user.email])
        email.send()
    except Exception as e:
        raise e

