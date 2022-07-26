from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import NewsletterUsers
from .forms import NewsletterUserSignUpForm
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
import json


def aboutus(request):
    """ A view to return the index page """

    return render(request, 'aboutus/aboutus.html')


def sitemap(request):
    """ A view to return the index page """

    return render(request, 'aboutus/sitemap.html')


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Sorry, This email \
            already exist.')

        else:
            instance.save()
            messages.success(request, 'Your are successfully subscribed \
        ')

            email = request.POST.get('email')
            html_message = render_to_string(
                'aboutus/confirmation_emails/newsletter_subscribe_confirmation.html',
                {'name': request.user.first_name})
            plain_message = strip_tags(html_message)

            send_mail(
                'Computer World',
                plain_message,
                'computer_world@yahoo.com',
                [email],
                fail_silently=False,
                html_message=html_message,
            )

    context = {
        'form': form,
    }
    return render(request, 'aboutus/sign_up.html')


def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            NewsletterUsers.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your are successfully unsubscribe \
        ')

            email = request.POST.get('email')
            html_message = render_to_string(
                'aboutus/confirmation_emails/newsletter_unsubscribe_confirmation.html',
                {'name': request.user.first_name})
            plain_message = strip_tags(html_message)

            send_mail(
                'Computer World',
                plain_message,
                'computer_world@yahoo.com',
                [email],
                fail_silently=False,
                html_message=html_message,
            )

        else:
            messages.error(request, 'sorry but we did not find your email \
        ')

    context = {
        'form': form,
    }
    return render(request, 'aboutus/unsubscribe.html')
