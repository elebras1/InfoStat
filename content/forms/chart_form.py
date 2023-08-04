from django import forms


class CourbeForm(forms.Form):
    titre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full",
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


CourbeFormSet = forms.formset_factory(
    CourbeForm, extra=1, can_delete=True, can_delete_extra=True
)
