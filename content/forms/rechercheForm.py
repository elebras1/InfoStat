from django import forms


class RechercheForm(forms.Form):
    result = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "Rechercher un article, une infographie...",
            }
        ),
    )

    CHOICES = (
        ("pub_date", "Date de publication"),
        ("populaire", "Populaire"),
    )
    selection = forms.ChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white",
            }
        ),
    )
