from django.contrib.auth import views as auth_views
from django.urls import path

from account.views import profile, register, CustomLogoutView

urlpatterns = [
    path('register', register, name='register_user'),
    path('login', auth_views.LoginView.as_view(
        template_name='account/login.html'
    ), name='login_view'),
    path('logout', CustomLogoutView.as_view(
        template_name='account/logged_out.html'
    ), name='logout_view'),

    path('profile', profile, name='account_profile')
]
