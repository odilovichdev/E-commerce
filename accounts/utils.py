# domain.uz/url/uuid64/token/(change password)

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from asyncio.log import logger
from django.contrib.auth.tokens import default_token_generator


def get_link(user, request, redirect_url:str="activate") -> str:

    try: 
        domain = get_current_site(request).domain
        uuid64 = urlsafe_base64_encode(force_bytes(user.id))
        token = default_token_generator.make_token(user)
        return f"http://{domain}/auth/{redirect_url}/{uuid64}/{token}"
    except Exception as e:
        logger.error(e)
        raise e


