"""legacybook_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core.views import logger_health_check
from marketing.views import homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="homepage"),
    path("account/", include("account.urls")),
    path("logger-health-check", logger_health_check),
    path("graveyard/", include("graveyard.urls", namespace="graveyard"))
]
