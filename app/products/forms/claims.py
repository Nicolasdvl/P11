"""
Django form for user claims.

Python class to build a form.
"""
from django import forms
from products.models import Claim


class ClaimForm(forms.ModelForm):

    name = forms.CharField(
        label="Nom du produit",
        widget=forms.TextInput(attrs={"id": "name", "class": "claim-form"}),
    )
    code = forms.CharField(
        label="Référence du produit",
        widget=forms.TextInput(attrs={"id": "code", "class": "claim-form"}),
        required=False,
    )
    brand = forms.CharField(
        label="Marque du fabricant",
        widget=forms.TextInput(attrs={"id": "brand", "class": "claim-form"}),
        required=False,
    )
    user_comment = forms.CharField(
        label="Informations complémentaires",
        widget=forms.TextInput(
            attrs={"id": "user_comment", "class": "claim-form"}
        ),
        required=False,
    )

    class Meta:
        model = Claim
        fields = ("name", "code", "brand", "user_comment")
