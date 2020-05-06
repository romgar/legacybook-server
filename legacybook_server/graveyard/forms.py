from django import forms

from graveyard.models import Decedent

class DecedentForm(forms.ModelForm):
    class Meta:
        model = Decedent
        fields = '__all__'
