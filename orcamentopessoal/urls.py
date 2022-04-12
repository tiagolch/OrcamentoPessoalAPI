from django.urls import path
from orcamentopessoal import views

urlpatterns = [
    path('dashboard/', views.Dashboard, name='dashboard'),
]