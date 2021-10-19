from django import forms
from core.models import Acao, Locacao_Acao, TipoLocacao


class Locacao_AcaoModelForm(forms.ModelForm):

    class Meta:
        model = Locacao_Acao
        fields = ['tipo_locacao', 'acao', 'memorial', 'status']


class AcaoModelForm(forms.ModelForm):

    class Meta:
        model = Acao
        fields = ['nome', 'descricao', 'observacoes', 'data_base', 'projeto', 'linguagem', 'local']


class TipoLocacaoModelForm(forms.ModelForm):

    class Meta:
        model = TipoLocacao
        fields = ['descricao']
