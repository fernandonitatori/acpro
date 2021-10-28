from django import forms
from core.models import Acao, Locacao_Acao, TipoLocacao, Memorial, Compras_Locacao, Sede, Contrato_Locacao, Pagamento,\
                        Cronograma


class LocacaoAcaoModelForm(forms.ModelForm):

    class Meta:
        model = Locacao_Acao
        fields = ['tipo_locacao', 'acao', 'memorial', 'status', 'status_geral']


class AcaoModelForm(forms.ModelForm):

    class Meta:
        model = Acao
        fields = ['nome', 'descricao', 'observacoes', 'data_base', 'projeto', 'linguagem', 'local']


class TipoLocacaoModelForm(forms.ModelForm):

    class Meta:
        model = TipoLocacao
        fields = ['descricao']


class MemorialModelForm(forms.ModelForm):

    class Meta:
        model = Memorial
        fields = ['descricao', 'data_memorial']


class ComprasLocacaoModelForm(forms.ModelForm):

    class Meta:
         model = Compras_Locacao
         fields = ['descricao', 'numero', 'data', 'observacoes', 'locacao', 'trp', 'status', 'sede']


class SedeModelForm(forms.ModelForm):

    class Meta:
         model = Sede
         fields = ['descricao', 'numero', 'dataminuta', 'datadca', 'anotacoes', 'licitacao', 'locacao', 'status']


class ContratoLocacaoModelForm(forms.ModelForm):

    class Meta:
         model = Contrato_Locacao
         fields = ['descricao', 'processo', 'dataprocesso', 'instrcontratual', 'datacontrato', 'valorservico',
                   'valorlocacao', 'pagto', 'locacao', 'status']


class PagamentoModelForm(forms.ModelForm):
    class Meta:
         model = Pagamento
         fields = ['descricao', 'tipo_pagto', 'atividade', 'parcela', 'qtde_parcelas', 'valor', 'dataprevnota',
                   'tiponota', 'numnota', 'dataemissnota', 'serienota', 'xml', 'anotacoes']






















