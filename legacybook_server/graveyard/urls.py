from django.contrib.auth import views as auth_views
from django.urls import path

from graveyard.views import person_erasing, register_decedent


app_name = 'graveyard'
urlpatterns = [
    path('register-decedent', register_decedent, name='register_decedent'),
    path('person-erasing', person_erasing, name='person_erasing'),
]
