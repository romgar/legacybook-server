from django.contrib.auth import views as auth_views
from django.urls import path

from marketing.views import erasing_info, foresee


app_name = 'marketing'
urlpatterns = [
    path('erasing-info', erasing_info, name='erasing_info'),
    path('foresee', foresee, name='foresee')
]
