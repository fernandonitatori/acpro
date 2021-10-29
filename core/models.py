from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateTimeField('Data e hora de criação', auto_now_add=True)
    modificado = models.DateField('Data e hora de modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Parametro(Base):
    descricao = models.CharField('Descrição', max_length=50)
    valor = models.CharField('Valor', max_length=50)
    observacoes = models.CharField('Observaçoes', max_length=100)

    class Meta:
        verbose_name = 'Parâmetro'
        verbose_name_plural = 'Parâmetros'

    def __str__(self):
        return self.descricao


class Local(Base):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.descricao


class Linguagem(Base):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Linguagem'
        verbose_name_plural = 'Linguagens'

    def __str__(self):
        return self.descricao


class Projeto(Base):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.descricao


class TipoLocacao(Base):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Tipo de Locação'
        verbose_name_plural = 'Tipos de Locação'

    def __str__(self):
        return self.descricao


class Tipo_Status(Base):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Tipo de Status'
        verbose_name_plural = 'Tipos de Status'

    def __str__(self):
        return self.descricao


class Status(Base):
    tipo_status = models.ForeignKey('Tipo_Status', verbose_name='tipo de Status', null=True, on_delete=models.SET_NULL)
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.descricao


class Memorial(Base):
    descricao = models.CharField('Descrição', max_length=50)
    data_memorial = models.DateField('Data do Memorial')

    class Meta:
        verbose_name = 'Memorial'
        verbose_name_plural = 'Memoriais'

    def __str__(self):
        return self.descricao


class Periodo(Base):
    etapa = models.CharField('Etapa', max_length=50)
    data_inicio = models.DateField('Data de Início')
    data_termino = models.DateField('Data de Término')
    locacao_acao = models.ForeignKey('Locacao_Acao', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'

    def __str__(self):
        return self.etapa


class Acao(Base):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=100, default='', blank=True)
    observacoes = models.CharField('Observações', max_length=100, default='', blank=True)
    data_base = models.DateField('Data Base')
    projeto = models.ForeignKey('Projeto', verbose_name='projeto', null=True, on_delete=models.SET_NULL, default='', blank=True)
    linguagem = models.ForeignKey('Linguagem', verbose_name='linguagem', null=True, on_delete=models.SET_NULL)
    local = models.ForeignKey('Local', verbose_name='local', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'

    def __str__(self):
        return self.nome


class Locacao_Acao(Base):
    tipo_locacao = models.ForeignKey('TipoLocacao', verbose_name='tipo de Locaçao', null=True, on_delete=models.SET_NULL)
    acao = models.ForeignKey('Acao', verbose_name='açao', null=True, on_delete=models.SET_NULL)
    memorial = models.ForeignKey('Memorial', verbose_name='memorial', null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey('Status', verbose_name='status', related_name='Status', null=True, on_delete=models.SET_NULL)
    status_geral = models.ForeignKey('Status', verbose_name='status geral', null=True, on_delete=models.SET_NULL)
    descricao = models.CharField('Descriçao', max_length=50)

    class Meta:
        verbose_name = 'Solicitação de Locação'
        verbose_name_plural = 'Solicitações de Locação'

    def __str__(self):
        return str(self.descricao)


class TRP(Base):
    numeroTRP = models.IntegerField('Número da TRP')
    descricao = models.CharField('Descrição', max_length=50)
    data_fim_contrato = models.DateField('Data Final do Contrato')
    data_fim_contrato_pror = models.DateField('Data Final do Contrato prorrogado')
    observacoes = models.CharField('Observaçoes', max_length=100)

    class Meta:
        verbose_name = 'TRP'
        verbose_name_plural = 'TRPs'

    def __str__(self):
        return self.descricao


class Fornecedor(Base):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=50)
    site = models.CharField('Site', max_length=100)
    observacoes = models.CharField('Observaçoes', max_length=100)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome


class CatFornecedor(Base):
    descricao = models.CharField('Descrição', max_length=50)
    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Categoria de Fornecedor'
        verbose_name_plural = 'Categorias de Fornecedores'

    def __str__(self):
        return self.descricao


class EndFornecedor(Base):
    logradouro = models.CharField('Logradouro', max_length=60)
    numero = models.IntegerField('Numero')
    complemento = models.CharField('Complemento', max_length=60)
    CEP = models.CharField('CEP', max_length=10)
    bairro = models.CharField('Bairro', max_length=60)
    cidade = models.CharField('Cidade', max_length=60)
    estado = models.CharField('Estado', max_length=60)
    pais = models.CharField('Pais', max_length=60)
    fornecedor = models.ForeignKey(Fornecedor,null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Endereço de Fornecedor'
        verbose_name_plural = 'Endereços de Fornecedores'

    def __str__(self):
        return f'{self.id} {self.logradouro} {self.numero}'


class ContFornecedor(Base):
    nome = models.CharField('Nome', max_length=60)
    telefone = models.CharField('Telefone', max_length=10)
    email = models.CharField('E-mail', max_length=60)
    observacoes = models.CharField('Observações', max_length=10)
    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Contato de Fornecedor'
        verbose_name_plural = 'Contatos de Fornecedores'

    def __str__(self):
        return self.nome


class Compras_Locacao(Base):
    descricao = models.CharField('Descrição', max_length=60)
    numero = models.CharField('Número', max_length=50)
    data = models.DateField('Data')
    observacoes = models.CharField('Observaçoes', null=True, max_length=100, default='',blank=False)
    locacao = models.ForeignKey(Locacao_Acao, verbose_name='ação', null=True, on_delete=models.SET_NULL)
    trp = models.ForeignKey(TRP, verbose_name='tRP', null=True, on_delete=models.SET_NULL, blank=False)
    status = models.ForeignKey(Status, verbose_name='status', null=True, on_delete=models.SET_NULL)
    sede = models.BooleanField('Sede')

    class Meta:
        verbose_name = 'Compras - Locaçao'
        verbose_name_plural = 'Compras - Locaçao'

    def __str__(self):
        return self.descricao


class Orcamento(Base):
    compras_loc = models.ForeignKey(Compras_Locacao, null=True, on_delete=models.SET_NULL)
    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete=models.SET_NULL)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    observacoes = models.CharField('Observaçoes', max_length=100)

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

    def __str__(self):
        return f'{self.id} {self.valor}'


class Licitacao(Base):
    descricao = models.CharField('Descrição', max_length=50)
    dataabertura = models.DateField('Data de Abertura')
    datapregao = models.DateField('Data do Pregão')
    dataassinatura = models.DateField('Data da Assinatura')
    datahomologacao = models.DateField('Data de Homologação')
    vencedor = models.CharField('Vencedor', max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Licitação'
        verbose_name_plural = 'Licitações'

    def __str__(self):
        return self.descricao


class Sede(Base):
    descricao = models.CharField('Descrição', max_length=50)
    numero = models.CharField('Número', max_length=50)
    dataminuta = models.DateField('Data Minuta')
    datadca = models.DateField('Data DCA')
    anotacoes = models.CharField('Anotaçoes', max_length=100)
    licitacao = models.ForeignKey(Licitacao, verbose_name='Licitação', null=True, on_delete=models.SET_NULL)
    locacao = models.ForeignKey(Locacao_Acao, verbose_name='Solicitação', null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, verbose_name='Status', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.descricao


class Aprovacao(Base):
    setor = models.CharField('Observaçoes', max_length=50)
    data = models.DateField('Data')
    sede = models.ForeignKey(Sede, verbose_name='Sede', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Aprovaçao'
        verbose_name_plural = 'Aprovaçoes'

    def __str__(self):
        return f'{self.id} {self.setor} {self.sede}'


class Cronograma(Base):
    locacao = models.ForeignKey(Locacao_Acao, verbose_name='Solicitação', null=True, on_delete=models.SET_NULL)
    atividade = models.CharField('Atividade', max_length=100)
    datainicio = models.DateField('Data Inicial')
    datafim = models.DateField('Data Final')
    anotacoes = models.CharField('Anotaçoes', max_length=100, null=True, blank=True)
    status = models.ForeignKey(Status, verbose_name='Status', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Cronogramas'
        verbose_name_plural = 'Cronogramas'

    def __str__(self):
        return self.atividade


class TipoPagto(Base):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Tipo de Pagamento'
        verbose_name_plural = 'Tipos de Pagamento'

    def __str__(self):
        return self.descricao


class Pagamento(Base):
    descricao = models.CharField('Descrição', max_length=50)
    tipo_pagto = models.ForeignKey(TipoPagto, verbose_name='Tipo de Pagamento', null=True, on_delete=models.SET_NULL)
    atividade = models.CharField('Atividade', max_length=100)
    parcela = models.DecimalField('Parcela', max_digits=10,decimal_places=2)
    qtde_parcelas = models.IntegerField('Quantidade de Parcelas')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    dataprevnota = models.DateField('Data Prev Nota')
    tiponota = models.CharField('Tipo da nota', max_length=50)
    numnota = models.IntegerField('Numero da Nota')
    dataemissnota = models.DateField('Data de Emisso da Nota')
    serienota = models.CharField('Série da Nota', max_length=100)
    xml = models.CharField('XML', max_length=100)
    anotacoes = models.CharField('Anotaçoes', max_length=100)
    locacao = models.ForeignKey(Locacao_Acao, verbose_name='Solicitação', null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, verbose_name='Status', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return self.descricao


class Contrato_Locacao(Base):
    descricao = models.CharField('Descrição', max_length=50)
    processo = models.CharField('Processo', max_length=50)
    dataprocesso = models.DateField('Data do Processo')
    instrcontratual = models.CharField('Instrumento Contratual', max_length=50)
    datacontrato = models.DateField('Data do Contrato')
    valorservico = models.DecimalField('Valor do Serviço', max_digits=10, decimal_places=2)
    valorlocacao = models.DecimalField('Valor da Locação', max_digits=10, decimal_places=2)
    locacao = models.ForeignKey(Locacao_Acao, verbose_name='Solicitação', null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, verbose_name='Status', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Contrato Locação'
        verbose_name_plural = 'Contratos Locação'

    def __str__(self):
        return self.descricao
