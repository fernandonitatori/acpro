from django.test import TestCase
from model_mommy import mommy


class ParametroTestCase(TestCase):

    def setUp(self):
        self.parametro = mommy.make('Parametro')

    def test_str(self):
        self.assertEquals(str(self.parametro), self.parametro.descricao)


class LocalTestCase(TestCase):

    def setUp(self):
        self.local = mommy.make('Local')

    def test_str(self):
        self.assertEquals(str(self.local), self.local.descricao)


class LinguagemTestCase(TestCase):

    def setUp(self):
        self.linguagem = mommy.make('Linguagem')

    def test_str(self):
        self.assertEquals(str(self.linguagem), self.linguagem.descricao)


class ProjetoTestCase(TestCase):

    def setUp(self):
        self.projeto = mommy.make('Projeto')

    def test_str(self):
        self.assertEquals(str(self.projeto), self.projeto.descricao)


class TipoLocacaoTestCase(TestCase):

    def setUp(self):
        self.tipoLocacao = mommy.make('TipoLocacao')

    def test_str(self):
        self.assertEquals(str(self.tipoLocacao), self.tipoLocacao.descricao)


class Tipo_StatusTestCase(TestCase):

    def setUp(self):
        self.tipostatus = mommy.make('Tipo_Status')

    def test_str(self):
        self.assertEquals(str(self.tipostatus), self.tipostatus.descricao)


class StatusTestCase(TestCase):

    def setUp(self):
        self.status = mommy.make('Status')

    def test_str(self):
        self.assertEquals(str(self.status), self.status.descricao)


class MemorialTestCase(TestCase):

    def setUp(self):
        self.memorial = mommy.make('Memorial')

    def test_str(self):
        self.assertEquals(str(self.memorial), self.memorial.descricao)


class PeriodoTestCase(TestCase):

    def setUp(self):
        self.periodo = mommy.make('Periodo')

    def test_str(self):
        self.assertEquals(str(self.periodo), self.periodo.etapa)


class AcaoTestCase(TestCase):

    def setUp(self):
        self.acao = mommy.make('Acao')

    def test_str(self):
        self.assertEquals(str(self.acao), self.acao.nome)


class Locacao_AcaoTestCase(TestCase):

    def setUp(self):
        self.locacao = mommy.make('Locacao_Acao')

    def test_str(self):
        self.assertEquals(str(self.locacao), self.locacao.descricao)


class TRPTestCase(TestCase):

    def setUp(self):
        self.trp = mommy.make('TRP')

    def test_str(self):
        self.assertEquals(str(self.trp), self.trp.descricao)


class FornecedorTestCase(TestCase):

    def setUp(self):
        self.fornecedor = mommy.make('Fornecedor')

    def test_str(self):
        self.assertEquals(str(self.fornecedor), self.fornecedor.nome)


class CatFornecedorTestCase(TestCase):

    def setUp(self):
        self.catfornecedor = mommy.make('CatFornecedor')

    def test_str(self):
        self.assertEquals(str(self.catfornecedor), self.catfornecedor.descricao)

class EndFornecedorTestCase(TestCase):

    def setUp(self):
        self.endfornecedor = mommy.make('EndFornecedor')

    def test_str(self):
        self.assertEquals(str(self.endfornecedor), self.endfornecedor.logradouro)


class ContFornecedorTestCase(TestCase):

    def setUp(self):
        self.contfornecedor = mommy.make('ContFornecedor')

    def test_str(self):
        self.assertEquals(str(self.contfornecedor), self.contfornecedor.nome)


class Compras_LocacaoTestCase(TestCase):

    def setUp(self):
        self.compras = mommy.make('Compras_Locacao')

    def test_str(self):
        self.assertEquals(str(self.compras), self.compras.descricao)


class OrcamentoTestCase(TestCase):

    def setUp(self):
        self.orcamento = mommy.make('Orcamento')

    def test_str(self):
        self.assertEquals(str(self.orcamento), self.orcamento.observacoes)


class LicitacaoTestCase(TestCase):

    def setUp(self):
        self.licitacao = mommy.make('Licitacao')

    def test_str(self):
        self.assertEquals(str(self.licitacao), self.licitacao.descricao)


class SedeTestCase(TestCase):

    def setUp(self):
        self.sede = mommy.make('Sede')

    def test_str(self):
        self.assertEquals(str(self.sede), self.sede.descricao)


class AprovacaoTestCase(TestCase):

    def setUp(self):
        self.aprovacao = mommy.make('Aprovacao')

    def test_str(self):
        self.assertEquals(str(self.aprovacao), self.aprovacao.descricao)


class CronogramaTestCase(TestCase):

    def setUp(self):
        self.cronograma = mommy.make('Cronograma')

    def test_str(self):
        self.assertEquals(str(self.cronograma), self.cronograma.atividade)


class TipoPagtoTestCase(TestCase):

    def setUp(self):
        self.tipopagto = mommy.make('TipoPagto')

    def test_str(self):
        self.assertEquals(str(self.tipopagto), self.tipopagto.descricao)


class PagamentoTestCase(TestCase):

    def setUp(self):
        self.pagamento = mommy.make('Pagamento')

    def test_str(self):
        self.assertEquals(str(self.pagamento), self.pagamento.descricao)


class Contrato_LocacaoTestCase(TestCase):

    def setUp(self):
        self.contr = mommy.make('Contrato_Locacao')

    def test_str(self):
        self.assertEquals(str(self.contr), self.contr.descricao)







