from functools import partial

from django import forms

from graveyard.models import Decedent


CustomDateInput = partial(forms.DateInput, {'class': 'datepicker'})

class DecedentForm(forms.ModelForm):

    class Meta:
        model = Decedent
        fields = '__all__'
        widgets = {
            'date_of_birth': CustomDateInput(),
            'date_of_death': CustomDateInput(),
        }
