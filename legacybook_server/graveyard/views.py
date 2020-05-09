from django.shortcuts import render
from django.contrib import messages

from graveyard.forms import DecedentForm

# Create your views here.
def register_decedent(request):
    decedent_form = DecedentForm()
    if request.method == 'POST':
        decedent_form = DecedentForm(request.POST)
        if decedent_form.is_valid():
            decedent_form.save()
            return render(request, 'graveyard/register_decedent_successful.html')

    return render(request, 'graveyard/register_decedent.html', {
        'decedent_form': decedent_form
    })
