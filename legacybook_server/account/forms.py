from django.forms import ModelForm

from account.models import User


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
