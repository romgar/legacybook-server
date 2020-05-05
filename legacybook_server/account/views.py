
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render

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

    register_form = RegisterUserForm()
    if request.method == 'POST':
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return render(request, 'account/register_success.html', {
                'register_form': register_form
            })

    return render(request, 'account/register.html', {
        'register_form': register_form
    })


@login_required
def profile(request):
    return render(request, 'account/profile.html')
