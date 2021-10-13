from django.contrib import admin
from .models import Fornecedor, Parametro, Local, Linguagem, Projeto, TipoLocacao, Tipo_Status, Status, Memorial, Periodo, Acao, Locacao_Acao

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'site','observacoes',]

@admin.register(Parametro)
class ParametroAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'valor', 'observacoes', ]

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ['descricao',]

@admin.register(Linguagem)
class LinguagemAdmin(admin.ModelAdmin):
    list_display = ['descricao',]

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['descricao',]

@admin.register(TipoLocacao)
class TipoLocacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao',]

@admin.register(Tipo_Status)
class Tipo_StatusAdmin(admin.ModelAdmin):
    list_display = ['descricao',]

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['descricao','tipo_status',]

@admin.register(Memorial)
class MemorialAdmin(admin.ModelAdmin):
    list_display = ['descricao','data_memorial',]

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['etapa','data_inicio','data_termino','locacao_acao',]

@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao','observacoes','data_base','projeto','linguagem','local',]


@admin.register(Locacao_Acao)
class Locacao_AcaoAdmin(admin.ModelAdmin):
    list_display = ['tipo_locacao','acao','memorial','status',]





