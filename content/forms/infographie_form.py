from django import forms
from ..models import Infographie


class InfographieForm(forms.ModelForm):
    class Meta:
        model = Infographie
        fields = [
            "titre",
            "description",
            "source",
            "theme",
            "region",
            "periode_enquete",
        ]

    type_graphique = forms.ChoiceField(
        choices=(
            ("line", "Courbe"),
            ("pie", "Secteurs"),
            ("scatter", "Nuage de points"),
            ("bar", "Barres"),
        )
    )

    x_titre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full",
                "value": "x",
            }
        ),
    )

    y_titre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full",
                "value": "y",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields_class_text = "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
        self.fields_class_text_area = "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 h-28"
        self.fields_class_select = "border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

        self.fields["titre"].widget.attrs["class"] = self.fields_class_text
        self.fields["description"].widget.attrs["class"] = self.fields_class_text_area
        self.fields["periode_enquete"].widget.attrs["class"] = self.fields_class_text
        self.fields["source"].widget.attrs["class"] = self.fields_class_text
        self.fields["theme"].widget.attrs["class"] = self.fields_class_select
        self.fields["region"].widget.attrs["class"] = self.fields_class_select
        self.fields["type_graphique"].widget.attrs["class"] = self.fields_class_select

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
        if len(description) > 3000:
            raise forms.ValidationError(
                "La description ne peut pas dépasser 3000 caractères."
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

    def clean_periode_enquete(self):
        periode_enquete = self.cleaned_data.get("periode_enquete")
        if len(periode_enquete) > 12:
            raise forms.ValidationError(
                "La période d'enquête ne peut pas dépasser 12 caractères."
            )
        elif len(periode_enquete) < 1:
            raise forms.ValidationError(
                "La période d'enquête doit contenir au minimum 1 caractère."
            )
        return periode_enquete

    def clean_x_titre(self):
        x_titre = self.cleaned_data.get("x_titre")
        if len(x_titre) > 40:
            raise forms.ValidationError(
                "La titre de l'axe des abscisses d'enquête ne peut pas dépasser 40 caractères."
            )
        elif len(x_titre) < 1:
            raise forms.ValidationError(
                "La titre de l'axe des abscisses doit contenir au minimum 1 caractère."
            )
        return x_titre

    def clean_y_titre(self):
        y_titre = self.cleaned_data.get("y_titre")
        if len(y_titre) > 40:
            raise forms.ValidationError(
                "La titre de l'axe des ordonnées d'enquête ne peut pas dépasser 40 caractères."
            )
        elif len(y_titre) < 1:
            raise forms.ValidationError(
                "La titre de l'axe des ordonnées doit contenir au minimum 1 caractère."
            )
        return y_titre
