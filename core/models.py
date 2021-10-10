from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de criação', auto_now=True)
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
