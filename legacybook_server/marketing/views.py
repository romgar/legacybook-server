from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'marketing/index.html')


def erasing_info(request):
    return render(request, 'marketing/erasing_info.html')
