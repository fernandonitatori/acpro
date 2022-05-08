from rest_framework import serializers

from .models import Locacao_Acao

class Locacao_AcaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Locacao_Acao
        fields = ('id', 'tipo_locacao', 'acao', 'memorial', 'status', 'status_geral', 'descricao', 'prazo', 'criado', 'modificado', 'ativo')
