from django.urls import path
from orcamentopessoal import views

urlpatterns = [
    path('receitas/', views.ReceitaList, name='receita_list'),
]