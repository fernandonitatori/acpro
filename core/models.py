from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


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
    tipo_status = models.ForeignKey('Tipo_Status',verbose_name='tipo de Status',on_delete=models.CASCADE,default='')
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
    locacao_acao = models.ForeignKey('Locacao_Acao', on_delete=models.SET_DEFAULT,default=99)

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'

    def __str__(self):
        return self.descricao

class Acao(Base):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=100)
    observacoes = models.CharField('Observações', max_length=100)
    data_base = models.DateField('Data Base')
    projeto = models.ForeignKey('Projeto', verbose_name='projeto',on_delete=models.SET_DEFAULT,default='')
    linguagem = models.ForeignKey('Linguagem', verbose_name='linguagem',on_delete=models.SET_DEFAULT,default='')
    local = models.ForeignKey('Local', verbose_name='local',on_delete=models.SET_DEFAULT,default='')

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'

    def __str__(self):
        return self.nome

class Locacao_Acao(Base):
    tipo_locacao = models.ForeignKey('TipoLocacao',verbose_name='tipo de Locaçao',on_delete=models.CASCADE)
    acao = models.ForeignKey('Acao',verbose_name='açao',on_delete=models.CASCADE)
    memorial = models.ForeignKey('Memorial',verbose_name='memorial',on_delete=models.CASCADE)
    status = models.ForeignKey('Status',verbose_name='status',on_delete=models.CASCADE)
    datasolicitacao = models.DateTimeField('Data da Solicitação',blank=True,auto_now_add=True)
    descricao = models.CharField('Descriçao', max_length=50, default='')

    class Meta:
        verbose_name = 'Solicitação de Locação'
        verbose_name_plural = 'Solicitações de Locação'

    def __str__(self):
        return self.descricao

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
        return f'{self.id} {self.descricao}'

class CatFornecedor(Base):
    descricao = models.CharField('Descrição', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=50)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE,default='')

    class Meta:
        verbose_name = 'Categoria de Fornecedor'
        verbose_name_plural = 'Categorias de Fornecedores'

    def __str__(self):
        return f'{self.id} {self.descricao} {self.cnpj}'

class EndFornecedor(Base):
    logradouro = models.CharField('Logradouro', max_length=60)
    numero = models.IntegerField('Numero')
    complemento = models.CharField('Complemento', max_length=60)
    CEP = models.CharField('CEP', max_length=10)
    bairro = models.CharField('Bairro', max_length=60)
    cidade = models.CharField('Cidade', max_length=60)
    estado = models.CharField('Estado', max_length=60)
    pais = models.CharField('Pais', max_length=60)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE,default='')

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
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE,default='')

    class Meta:
        verbose_name = 'Contato de Fornecedor'
        verbose_name_plural = 'Contatos de Fornecedores'

    def __str__(self):
        return f'{self.id} {self.nome} {self.telefone} {self.email}'

class Compras_Locacao(Base):
    descricao = models.CharField('Descrição', max_length=60)
    numero = models.IntegerField('Número')
    data = models.DateField('Data')
    observacoes = models.CharField('Observaçoes',max_length=100)
    locacao = models.ForeignKey(Locacao_Acao,verbose_name='ação',on_delete=models.CASCADE, default='')
    trp = models.ForeignKey(TRP, verbose_name='tRP',on_delete=models.CASCADE, default='')
    status = models.ForeignKey(Status,verbose_name='status',on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'Compras - Locaçao'
        verbose_name_plural = 'Compras - Locaçao'

    def __str__(self):
        return f'{self.id} {self.descricao} {self.numero} {observacoes} {status}'

class Orcamento(Base):
    compras_loc = models.ForeignKey(Compras_Locacao,on_delete=models.CASCADE,default='')
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE,default='')
    valor = models.DecimalField('Valor',max_digits=10,decimal_places=2)
    observacoes = models.CharField('Observaçoes',max_length=100)
    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

    def __str__(self):
        return f'{self.id} {self.valor}'

class Licitacao(Base):
    dataabertura = models.DateField('Data de Abertura')
    datapregao = models.DateField('Data do Pregão')
    dataassinatura = models.DateField('Data da Assinatura')
    datahomologacao = models.DateField('Data de Homologação')
    vencedor = models.CharField('Vencedor', max_length=50)
    valor = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        verbose_name = 'Licitação'
        verbose_name_plural = 'Licitações'

    def __str__(self):
        return f'{self.id} {self.dataabertura} {self.datapregao} {self.dataassinatura} {self.datahomologacao} {self.vencedor} {self.valor} '

class DCA(Base):
    numero = models.CharField('Vencedor', max_length=50)
    dataminuta = models.DateField('Data Minuta')
    datadca = models.DateField('Data DCA')
    anotacoes = models.CharField('Anotaçoes', max_length=100)
    licitacao = models.ForeignKey(Licitacao,verbose_name='Licitação',on_delete=models.CASCADE,default='')
    locacao_acao = models.ForeignKey(Locacao_Acao, verbose_name='Solicitação', on_delete=models.CASCADE, default='')
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'DCA'
        verbose_name_plural = 'DCAs'

    def __str__(self):
        return f'{self.id} {self.dataminuta} {self.datadca} {self.licitacao} {self.locacao_acao} {self.status}'

class Aprovacao(Base):
    setor = models.CharField('Observaçoes', max_length=50)
    data = models.DateField('Data')
    dca = models.ForeignKey(DCA,verbose_name='DCA',on_delete=models.CASCADE,default='')

    class Meta:
        verbose_name = 'Aprovaçao'
        verbose_name_plural = 'Aprovaçoes'

    def __str__(self):
        return f'{self.id} {self.setor} {self.dca}'

class Cronograma(Base):
    locacao_acao = models.ForeignKey(Locacao_Acao, verbose_name='Solicitação', on_delete=models.CASCADE, default='')
    atividade = models.CharField('Atividade', max_length=100)
    datainicio = models.DateField('Data Inicial')
    datafim = models.DateField('Data Final')
    anotacoes = models.CharField('Anotaçoes', max_length=100)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'Cronogramas'
        verbose_name_plural = 'Cronogramas'

    def __str__(self):
        return f'{self.id} {self.locacao_acao} {self.datainicio} {self.datafim} {self.anotacoes} {self.status}'

class TipoPagto(Base):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Tipo de Pagamento'
        verbose_name_plural = 'Tipos de Pagamento'

    def __str__(self):
        return f'{self.id} {self.descricao}'

class Pagamento(Base):
    tipo_pagto = models.ForeignKey(TipoPagto, verbose_name='Tipo de Pagamento', on_delete=models.CASCADE, default='')
    atividade = models.CharField('Atividade', max_length=100)
    parcela = models.DecimalField('Parcela',max_digits=10,decimal_places=2)
    qtde_parcelas = models.IntegerField('Quantidade de Parcelas')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    dataprevnota = models.DateField('Data Prev Nota')
    tiponota = models.CharField('Tipo da nota', max_length=5)
    numnota = models.IntegerField('Numero da Nota')
    dataemissnota = models.DateField('Data de Emisso da Nota')
    serienota = models.CharField('Série da Nota', max_length=100)
    xml = models.CharField('XML', max_length=100)
    anotacoes = models.CharField('Anotaçoes', max_length=100)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return f'{self.id} {self.tipo_pagto} {self.valor} {self.anotacoes}'

class Contrato_Locacao(Base):
    processo = models.CharField('Processo', max_length=50)
    dataprocesso = models.DateField('Data do Processo')
    instrcontratual = models.CharField('Instrumento Contratual', max_length=50)
    datacontrato = models.DateField('Data do Contrato')
    valorservico= models.DecimalField('Valor do Serviço', max_digits=10, decimal_places=2)
    valorlocacao = models.DecimalField('Valor da Locação', max_digits=10, decimal_places=2)
    pagto = models.ForeignKey(Pagamento, verbose_name='Pagamento', on_delete=models.CASCADE, default='')
    locacao_acao = models.ForeignKey(Locacao_Acao, verbose_name='Solicitação', on_delete=models.CASCADE, default='')
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'Contrato Locação'
        verbose_name_plural = 'Contratos Locação'

    def __str__(self):
        return f'{self.id} {self.processo} {self.dataprocesso} {self.datacontrato} {self.valorlocacao} {self.status}'
