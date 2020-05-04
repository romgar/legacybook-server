from django.shortcuts import render

from account.forms import RegisterUserForm


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
