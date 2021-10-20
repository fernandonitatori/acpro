from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Locacao_Acao, Acao, TipoLocacao, Memorial, Compras_Locacao, TRP, Orcamento, DCA, Licitacao, \
                    Contrato_Locacao, Pagamento, Cronograma, Aprovacao, Fornecedor, CatFornecedor, EndFornecedor, \
                    ContFornecedor, Tipo_Status, Status, Local, Linguagem, Projeto, TipoPagto

from .forms import TipoLocacaoModelForm, MemorialModelForm


class ListLocacaoAcaoView(ListView):
    model = Locacao_Acao
    template_name = 'locacao_acao_listview.html'
    queryset = Locacao_Acao.objects.all()
    context_object_name = 'locacoes'


class IndexView(TemplateView):
    template_name = 'index.html'


class SistemaView(TemplateView):
    template_name = 'sistema.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numsolicit'] = Locacao_Acao.objects.count()
        return context


class CreateSolicitView(CreateView):
    model = Locacao_Acao
    template_name = 'form_solicit_loc.html'
    fields = ['tipo_locacao', 'acao', 'memorial', 'status']
    success_url = reverse_lazy('sistema')


class ConsultaLocacaoAcaoView(UpdateView):
    model = Locacao_Acao
    template_name = 'locacao_acao_consulta.html'
    fields = ['tipo_locacao', 'acao', 'memorial', 'status']
    context_object_name = 'consulta'
    success_url = reverse_lazy('sistema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_chave'] = 'Solicitado'
        return context


class ListUpdLocacaoAcaoView(ListView):
    model = Locacao_Acao
    template_name = 'locacao_acao_updlistview.html'
    queryset = Locacao_Acao.objects.all()
    context_object_name = 'updlocacoes'


class CreateAcaoView(CreateView):
    model = Acao
    template_name = 'form_create_acao.html'
    fields = ['nome', 'descricao', 'observacoes', 'data_base', 'projeto', 'linguagem', 'local']
    success_url = reverse_lazy('sistema')


class CreateTipoLocView(CreateView):
    model = TipoLocacao
    template_name = 'form_create_tipoloc.html'
    fields = ['descricao']
    success_url = reverse_lazy('sistema')


class CreateMemorialView(CreateView):
    model = Memorial
    template_name = 'form_create_memorial.html'
    fields = ['descricao', 'data_memorial']
    success_url = reverse_lazy('sistema')


class CreateComprasLocView(CreateView):
    model = Compras_Locacao
    template_name = 'form_create_compras.html'
    fields = ['descricao', 'numero', 'data', 'observacoes', 'locacao', 'trp', 'status']
    success_url = reverse_lazy('sistema')


class CreateTRPView(CreateView):
    model = TRP
    template_name = 'form_create_trp.html'
    fields = ['numeroTRP', 'descricao', 'data_fim_contrato', 'data_fim_contrato_pror', 'observacoes']
    success_url = reverse_lazy('sistema')


class CreateOrcView(CreateView):
    model = Orcamento
    template_name = 'form_create_orc.html'
    fields = ['compras_loc', 'fornecedor', 'valor', 'observacoes']
    success_url = reverse_lazy('sistema')


class CreateDCAView(CreateView):
    model = DCA
    template_name = 'form_create_dca.html'
    fields = ['numero', 'dataminuta', 'datadca', 'anotacoes', 'licitacao', 'locacao_acao', 'status']
    success_url = reverse_lazy('sistema')


class CreateLicView(CreateView):
    model = Licitacao
    template_name = 'form_create_lic.html'
    fields = ['dataabertura', 'datapregao', 'dataassinatura', 'datahomologacao', 'vencedor', 'valor']
    success_url = reverse_lazy('sistema')


class CreateContrView(CreateView):
    model = Contrato_Locacao
    template_name = 'form_create_contrat.html'
    fields = ['processo', 'dataprocesso', 'instrcontratual', 'datacontrato', 'valorservico', 'valorlocacao', 'pagto',
              'locacao_acao', 'status']
    success_url = reverse_lazy('sistema')


class CreatePagtoView(CreateView):
    model = Pagamento
    template_name = 'form_create_pagto.html'
    fields = ['tipo_pagto', 'atividade', 'parcela', 'qtde_parcelas', 'valor', 'dataprevnota', 'tiponota', 'numnota',
              'dataemissnota', 'serienota', 'xml', 'anotacoes']
    success_url = reverse_lazy('sistema')


class CreateCronoView(CreateView):
    model = Cronograma
    template_name = 'form_create_crono.html'
    fields = ['locacao_acao', 'atividade', 'datainicio', 'datafim', 'anotacoes', 'status']
    success_url = reverse_lazy('sistema')


class CreateAprovView(CreateView):
    model = Aprovacao
    template_name = 'form_create_aprov.html'
    fields = ['setor', 'data', 'dca']
    success_url = reverse_lazy('sistema')


class CreateFornecView(CreateView):
    model = Fornecedor
    template_name = 'form_create_fornec.html'
    fields = ['nome', 'cnpj', 'site', 'observacoes']
    success_url = reverse_lazy('sistema')


class CreateCatFornecView(CreateView):
    model = CatFornecedor
    template_name = 'form_create_catfornec.html'
    fields = ['descricao', 'fornecedor']
    success_url = reverse_lazy('sistema')


class CreateEndFornecView(CreateView):
    model = EndFornecedor
    template_name = 'form_create_endfornec.html'
    fields = ['logradouro', 'numero', 'complemento', 'CEP', 'bairro', 'cidade', 'estado', 'pais', 'fornecedor']
    success_url = reverse_lazy('sistema')


class CreateContFornecView(CreateView):
    model = ContFornecedor
    template_name = 'form_create_contfornec.html'
    fields = ['nome', 'telefone', 'email', 'observacoes', 'fornecedor']
    success_url = reverse_lazy('sistema')


class CreateTipoStatusView(CreateView):
    model = Tipo_Status
    template_name = 'form_create_tipostatus.html'
    fields = ['descricao']
    success_url = reverse_lazy('sistema')


class CreateStatusView(CreateView):
    model = Status
    template_name = 'form_create_status.html'
    fields = ['tipo_status', 'descricao']
    success_url = reverse_lazy('sistema')


class CreateLocalView(CreateView):
    model = Local
    template_name = 'form_create_local.html'
    fields = ['descricao']
    success_url = reverse_lazy('sistema')


class CreateLinguagemView(CreateView):
    model = Linguagem
    template_name = 'form_create_ling.html'
    fields = ['descricao']
    success_url = reverse_lazy('sistema')


class CreateProjetoView(CreateView):
    model = Projeto
    template_name = 'form_create_proj.html'
    fields = ['descricao']
    success_url = reverse_lazy('sistema')


class CreateTipoPagtoView(CreateView):
    model = TipoPagto
    template_name = 'form_create_tipopagto.html'
    fields = ['descricao']
    success_url = reverse_lazy('sistema')


def salvatipoloc(request):
    descricao = request.POST.get('descricao')
    if TipoLocacao.objects.filter(descricao=descricao).exists():
        messages.error(request, "Tipo de locação já cadastrado!")
        return redirect('../add/')
    else:
        form = TipoLocacaoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../add/')

def salvamemorial(request):
    descricao = request.POST.get('descricao')
    if Memorial.objects.filter(descricao=descricao).exists():
        messages.error(request, "Memorial já cadastrado!")
        return redirect('../add/')
    else:
        form = MemorialModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../add/')
