from django import forms

from account.models import User


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
