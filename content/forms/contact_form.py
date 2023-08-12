from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full",
            }
        ),
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
            }
        ),
    )

    sujet = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
            }
        ),
    )

    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 h-28",
            }
        ),
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > 80:
            raise forms.ValidationError("Le nom ne peut pas dépasser 80 caractères.")
        elif len(name) < 12:
            raise forms.ValidationError(
                "Le nom doit contenir au minimum 12 caractères."
            )
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if len(email) > 100:
            raise forms.ValidationError("L'email ne peut pas dépasser 100 caractères.")
        return email

    def clean_sujet(self):
        sujet = self.cleaned_data.get("sujet")
        if len(sujet) > 100:
            raise forms.ValidationError("Le sujet ne peut pas dépasser 100 caractères.")
        elif len(sujet) < 10:
            raise forms.ValidationError(
                "Le sujet doit contenir au minimum 10 caractères."
            )
        return sujet

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) > 100:
            raise forms.ValidationError(
                "Le message ne peut pas dépasser 2000 caractères."
            )
        elif len(message) < 10:
            raise forms.ValidationError(
                "Le message doit contenir au minimum 10 caractères."
            )
        return message
