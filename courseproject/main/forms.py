from dataclasses import fields
from .models import Subs
from django.forms import ModelForm, TextInput


class SubForm(ModelForm):
    class Meta:
        model = Subs
        fields = ['MAIL'] 

        widgets = {
            "MAIL": TextInput(attrs={
                "class": "newsletter_input",
            })
        }