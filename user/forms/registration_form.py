from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Pseudo*", max_length=100)
    email = forms.CharField(label="Email*", max_length=100)
    last_name = forms.CharField(label="Prénom", max_length=100, required=False)
    first_name = forms.CharField(label="Nom", max_length=100, required=False)
    password = forms.CharField(label="Mot de passe*", max_length=128)
    password_confirmation = forms.CharField(
        label="Confirmation du mot de passe*", max_length=100
    )
