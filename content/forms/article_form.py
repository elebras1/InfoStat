from django import forms
from ..models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["titre", "description", "source", "theme", "region"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields_class_text = "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
        self.fields_class_select = "border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

        self.fields["titre"].widget.attrs["class"] = self.fields_class_text
        self.fields["description"].widget.attrs["class"] = self.fields_class_text
        self.fields["source"].widget.attrs["class"] = self.fields_class_text
        self.fields["theme"].widget.attrs["class"] = self.fields_class_select
        self.fields["region"].widget.attrs["class"] = self.fields_class_select

    def clean_titre(self):
        titre = self.cleaned_data.get("titre")
        if len(titre) > 80:
            raise forms.ValidationError("Le titre ne peut pas dépasser 80 caractères.")
        elif len(titre) < 5:
            raise forms.ValidationError(
                "Le titre doit contenir au minimum 5 caractères."
            )
        return titre

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) > 15000:
            raise forms.ValidationError(
                "La description ne peut pas dépasser 15 000 caractères."
            )
        elif len(description) < 5:
            raise forms.ValidationError(
                "La description doit contenir au minimum 5 caractères."
            )
        return description

    def clean_source(self):
        source = self.cleaned_data.get("source")
        if len(source) > 3000:
            raise forms.ValidationError(
                "La source ne peut pas dépasser 120 caractères."
            )
        elif len(source) < 5:
            raise forms.ValidationError(
                "La source doit contenir au minimum 5 caractères."
            )
        return source
