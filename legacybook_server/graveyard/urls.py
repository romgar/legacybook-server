from django.contrib.auth import views as auth_views
from django.urls import path

from graveyard.views import register_decedent


app_name = 'graveyard'
urlpatterns = [
    path('register-decedent', register_decedent, name='register_decedent'),
]
