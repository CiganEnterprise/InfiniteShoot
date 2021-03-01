from django import forms
from Gallery.models import ClientCatalogue
from .models import PART_OF_CATALOGUE


class ImageClientForm(forms.ModelForm):
    image_positioning = forms.ChoiceField(choices=PART_OF_CATALOGUE, initial="None of it")

    class Meta:
        model = ClientCatalogue

        fields = (
            'image_positioning',
        )
