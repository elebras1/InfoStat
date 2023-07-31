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
            ("scatter", "Nuage de points"),
            ("line", "Courbe"),
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

    x_valeurs = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full",
            }
        ),
    )

    y_valeurs = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full",
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
