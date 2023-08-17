from django import forms


class PasswordForm(forms.Form):
    password = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
                "type": "password",
            }
        ),
    )

    new_password = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
                "type": "password",
            }
        ),
    )

    new_password_confirmation = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
                "type": "password",
            }
        ),
    )

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) > 20:
            raise forms.ValidationError(
                "Le mot de passe ne peut pas dépasser 20 caractères."
            )
        return password

    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        if len(new_password) > 20:
            raise forms.ValidationError(
                "Le nouveau mot de passe ne peut pas dépasser 20 caractères."
            )
        elif len(new_password) < 8:
            raise forms.ValidationError(
                "Le nouveau mot de passe passe doit contenir au minimum 8 caractères."
            )
        return new_password

    def clean_new_password_confirmation(self):
        new_password_confirmation = self.cleaned_data.get("new_password_confirmation")
        if len(new_password_confirmation) > 20:
            raise forms.ValidationError(
                "Le nouveau mot de passe de confirmation ne peut pas dépasser 20 caractères."
            )
        elif len(new_password_confirmation) < 8:
            raise forms.ValidationError(
                "Le nouveau mot de passe de confirmation doit contenir au minimum 8 caractères."
            )
        return new_password_confirmation
