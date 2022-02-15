from django.contrib import admin
from .models import Receita, Despesa

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'get_data')
    list_filter = ('data',)
    search_fields = ('descricao',)

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'get_data')
    list_filter = ('data',)
    search_fields = ('descricao',)

