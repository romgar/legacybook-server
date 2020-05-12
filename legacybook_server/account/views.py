
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render

from account.forms import RegisterUserForm


class CustomLogoutView(LogoutView):

    def get_next_page(self):
        next_page = super(CustomLogoutView, self).get_next_page()
        messages.add_message(
            self.request, messages.SUCCESS,
            'Vous avez été déconnecté avec success!'
        )
        return next_page


def register(request):

    if request.user.is_authenticated:
        return redirect('account_profile')

    register_form = RegisterUserForm()
    if request.method == 'POST':
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS,
                    'Votre compte a été créé avec success!'
                )
                return redirect('account_profile')
            else:
                # Should never happen, as we just created this user
                # and we used the exact same email/password to create it
                # TODO: raise a proper log when configured.
                pass

    return render(request, 'account/register.html', {
        'register_form': register_form
    })


@login_required
def profile(request):
    return render(request, 'account/profile.html')
