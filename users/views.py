from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core import mail
from django.utils.html import strip_tags
from .forms import CustomUserCreationForm
from .tokens import account_activation_token

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register_form.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect(reverse("register_done"))
        return render(
            request, "users/register_form.html",
            {"form": form}
        )


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your Django Project Template user account.'
    html_message = render_to_string('users/register_email.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    plain_message = strip_tags(html_message)
    from_email = 'Django Project Template <{}>'.format(settings.EMAIL_FROM)
    to = user.email
    mail.send_mail(mail_subject, plain_message, from_email, [to], html_message=html_message)


class RegisterDone(TemplateView):
    template_name = "users/register_done.html"


def register_complete(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(
            request, "users/register_complete.html", {"validlink": True}
        )
    else:
        return render(
            request, "users/register_complete.html", {"validlink": False}
        )
