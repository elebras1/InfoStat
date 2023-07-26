from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms.contact_form import ContactForm
from user.models import User
from django.contrib import messages


def contact(request):
    superusers = User.objects.filter(is_superuser=True)
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            sujet = form.cleaned_data["sujet"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                for superuser in superusers:
                    send_mail(sujet, message, email, [superuser.email])
                messages.error(
                    request,
                    "Votre message a bien été envoyé.",
                )
            except BadHeaderError:
                return redirect("contact")
            form = ContactForm()
    return render(request, "contact.html", {"form": form})
