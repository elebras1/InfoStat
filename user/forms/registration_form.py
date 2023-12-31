from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }
        ),
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }
        ),
    )
    first_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }
        ),
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }
        ),
    )
    password_confirmation = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }
        ),
    )

    photo = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "block w-full mb-5 text-xs text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
            }
        ),
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) > 20:
            raise forms.ValidationError("Le pseudo ne peut pas dépasser 20 caractères.")
        elif len(username) < 2:
            raise forms.ValidationError(
                "Le pseudo doit contenir au minimum 2 caractères."
            )
        return username

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if len(last_name) > 60:
            raise forms.ValidationError(
                "Le nom de famille ne peut pas dépasser 60 caractères."
            )
        elif len(last_name) < 2:
            raise forms.ValidationError(
                "Le nom de famille doit contenir au minimum 2 caractères."
            )
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if len(first_name) > 60:
            raise forms.ValidationError("Le prénom ne peut pas dépasser 60 caractères.")
        elif len(first_name) < 2:
            raise forms.ValidationError(
                "Le prénom doit contenir au minimum 2 caractères."
            )
        return first_name

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) > 20:
            raise forms.ValidationError(
                "Le mot de passe ne peut pas dépasser 20 caractères."
            )
        elif len(password) < 2:
            raise forms.ValidationError(
                "Le mot de passe doit contenir au minimum 8 caractères."
            )
        return password

    def clean_password_confirmation(self):
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if len(password_confirmation) > 20:
            raise forms.ValidationError(
                "Le mot de passe ne peut pas dépasser 20 caractères."
            )
        elif len(password_confirmation) < 2:
            raise forms.ValidationError(
                "Le mot de passe doit contenir au minimum 8 caractères."
            )
        return password_confirmation

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")

        if photo:
            valid_extensions = [".png", ".jpeg", ".jpg"]
            file_extension = photo.name.split(".")[-1].lower()

            if file_extension not in valid_extensions:
                raise forms.ValidationError(
                    "Seuls les fichiers PNG et JPEG sont autorisés."
                )

        return photo
