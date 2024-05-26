from django.urls import path
from . import views as services_views

from django.conf import settings

urlpatterns = [
    path('', services_views.services, name="services"),
]
 