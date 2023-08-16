from django import forms
from ..models import Secteur


class SecteurForm(forms.ModelForm):
    class Meta:
        model = Secteur
        fields = [
            "nom",
            "description",
        ]

    illustration = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "block w-full mb-5 text-xs text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields_class_text = "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
        self.fields_class_text_area = "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 h-28"

        self.fields["nom"].widget.attrs["class"] = self.fields_class_text
        self.fields["description"].widget.attrs["class"] = self.fields_class_text_area

    def clean_nom(self):
        nom = self.cleaned_data.get("nom")
        if len(nom) > 80:
            raise forms.ValidationError(
                "Le nom du secteur ne peut pas dépasser 80 caractères."
            )
        elif len(nom) < 5:
            raise forms.ValidationError(
                "Le nom du secteur doit contenir au minimum 5 caractères."
            )
        return nom

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) > 3000:
            raise forms.ValidationError(
                "La description ne peut pas dépasser 3000 caractères."
            )
        elif len(description) < 5:
            raise forms.ValidationError(
                "La description doit contenir au minimum 5 caractères."
            )
        return description

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration")

        if illustration:
            valid_extensions = [".png", ".jpeg", ".jpg"]
            file_extension = illustration.name.split(".")[-1].lower()

            if file_extension not in valid_extensions:
                raise forms.ValidationError(
                    "Seuls les fichiers PNG et JPEG sont autorisés."
                )

        return illustration
