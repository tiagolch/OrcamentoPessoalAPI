from django.contrib import admin
from .models import Receita, Despesa, Categoria, Pessoa, Cartao


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'pessoa', 'get_data')
    list_filter = ('data', 'categoria', 'pessoa', 'cartao')
    search_fields = ('descricao',)

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'get_data')
    list_filter = ('data',)
    search_fields = ('descricao',)



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)


@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('bandeira', 'numero', 'vencimento', 'get_data')
    list_filter = ('vencimento',)
    search_fields = ('bandeira', 'numero')

