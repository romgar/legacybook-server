from django.contrib.auth import views as auth_views
from django.urls import path

from marketing.views import erasing_info


app_name = 'marketing'
urlpatterns = [
    path('erasing-info', erasing_info, name='erasing_info'),
]
