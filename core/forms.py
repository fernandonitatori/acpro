from django import forms
from core.models import Acao, Locacao_Acao

class Locacao_AcaoModelForm(forms.ModelForm):
    class Meta:
        model = Locacao_Acao
        fields = [__all__]

class AcaoModelForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = ['nome','descricao','observacoes','data_base','projeto','linguagem','local']



