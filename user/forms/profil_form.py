from django import forms
from django.contrib.auth.models import User


class ProfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "last_name",
            "first_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields_class = "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"

        self.fields["username"].widget.attrs["class"] = self.fields_class
        self.fields["email"].widget.attrs["class"] = self.fields_class
        self.fields["last_name"].widget.attrs["class"] = self.fields_class
        self.fields["first_name"].widget.attrs["class"] = self.fields_class

    photo = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "block w-full mb-5 text-xs text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
            }
        ),
    )
