from django.urls import path
from orcamentopessoal import views

urlpatterns = [
    path('', views.Home, name='home'),
]