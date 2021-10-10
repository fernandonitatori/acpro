from django.contrib import admin
from .models import Fornecedor, Parametro

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'site', 'observacoes', ]

@admin.register(Parametro)
class ParametroAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'valor', 'observacoes', ]
