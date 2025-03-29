from django import forms
from .models import *


# creating a form
class ConvertForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Link
        fields = ( 'url_long',)