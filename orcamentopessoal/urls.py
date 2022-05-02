from django.urls import path
from orcamentopessoal import views
from .api import api


urlpatterns = [
    path('', views.Home, name='home'),
    path('api/', api.urls )
]