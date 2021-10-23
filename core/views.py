from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages


from .models import Locacao_Acao, Acao, TipoLocacao, Memorial, Compras_Locacao, TRP, Orcamento, Sede, Licitacao, \
                    Contrato_Locacao, Pagamento, Cronograma, Aprovacao, Fornecedor, CatFornecedor, EndFornecedor, \
                    ContFornecedor, Tipo_Status, Status, Local, Linguagem, Projeto, TipoPagto

from .forms import TipoLocacaoModelForm, MemorialModelForm


class ListLocacaoAcaoView(ListView):
    model = Locacao_Acao
    template_name = 'locacao_acao_listview.html'
    queryset = Locacao_Acao.objects.all()
    context_object_name = 'locacoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tiposlocacao'] = TipoLocacao.objects.all()
        context['acoes'] = Acao.objects.all()
        context['memoriais'] = Memorial.objects.all()
        context['statuses'] = Status.objects.all()
        return context

class IndexView(TemplateView):
    template_name = 'index.html'


class SistemaView(TemplateView):
    template_name = 'sistema.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numsolicit'] = Locacao_Acao.objects.count()
        context['numcompras'] = Compras_Locacao.objects.count()
        return context


class CreateSolicitView(CreateView):
    model = Locacao_Acao
    template_name = 'form_solicit_loc.html'
    fields = ['tipo_locacao', 'acao', 'memorial', 'status_geral', 'descricao']
    success_url = reverse_lazy('sistema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tiposlocacao'] = TipoLocacao.objects.all()
        context['acoes'] = Acao.objects.all()
        context['memoriais'] = Memorial.objects.all()
        context['statuses'] = Status.objects.all()
        return context


class ConsultaLocacaoAcaoView(UpdateView):
    model = Locacao_Acao
    template_name = 'locacao_acao_consulta.html'
    fields = ['tipo_locacao', 'acao', 'memorial', 'status_geral']
    context_object_name = 'consulta'
    success_url = reverse_lazy('sistema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_chave_sol'] = 'Solicitado'
        context['status_compras_emaprov'] = 'Compras - Em Aprovação'
        context['status_compras_emorc'] = 'Compras - Aguardando orçamento'
        context['status_compras_orc'] = 'Compras - Orçado'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trps'] = TRP.objects.all()
        context['statuses'] = Status.objects.all()
        return context


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


class CreateSedeView(CreateView):
    model = Sede
    template_name = 'form_create_sede.html'
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


def consultalocacao(request):
    tipoloc = request.POST.get("tipo_locacao")
    acao = request.POST.get("acao")
    memorial = request.POST.get("memorial")
    statusgeral = request.POST.get("status_geral")

    criterio1 = False
    criterio2 = False
    criterio3 = False
    criterio4 = False

    if tipoloc != '':
        criterio1 = True
    if acao != '':
        criterio2 = True
    if memorial != '':
        criterio3 = True
    if statusgeral != '':
        criterio4 = True

    if criterio1 == True and criterio2 == False and criterio3 == False:
        locacoes = Locacao_Acao.objects.filter(tipo_locacao=tipoloc)
    if criterio1 == False and criterio2 == True and criterio3 == False:
        locacoes = Locacao_Acao.objects.filter(acao=acao)
    if criterio1 == False and criterio2 == False and criterio3 == True:
        locacoes = Locacao_Acao.objects.filter(memorial=memorial)
    if criterio1 == True and criterio2 == True and criterio3 == False:
        locacoes = Locacao_Acao.objects.filter(tipo_locacao=tipoloc,acao=acao)
    if criterio1 == True and criterio2 == False and criterio3 == True:
        locacoes = Locacao_Acao.objects.filter(tipo_locacao=tipoloc, memorial=memorial)
    if criterio1 == False and criterio2 == True and criterio3 == True:
        locacoes = Locacao_Acao.objects.filter(acao=acao, memorial=memorial)
    if criterio1 == True and criterio2 == True and criterio3 == True:
        locacoes = Locacao_Acao.objects.filter(tipo_locacao=tipoloc, acao=acao, memorial=memorial)
    if criterio4 == True:
        locacoes = Locacao_Acao.objects.filter(status_geral=statusgeral)
    if criterio1 == False and criterio2 == False and criterio3 == False and criterio4 == False:
        locacoes = Locacao_Acao.objects.all()

    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    statuses = Status.objects.all()
    context = {'locacoes': locacoes,
               'tiposlocacao': tiposlocacao,
               'acoes': acoes,
               'memoriais': memoriais,
               'statuses': statuses
               }
    return render(request, 'locacao_acao_listview.html', context)

def consultaumalocacao(request,pk):

    idpassado = pk
    print(idpassado)
    consulta = get_object_or_404(Locacao_Acao,id=pk)
    consultacompras = ''
    if Compras_Locacao.objects.filter(locacao=idpassado).exists():
        consultacompras = Compras_Locacao.objects.get(locacao=idpassado)
    statuses = Status.objects.all()
    trps = TRP.objects.all()
    context = {
            'consulta': consulta,
            'consultacompras': consultacompras,
            'status_chave_sol': 'Solicitado',
            'status_chave_compras': 'Compras - Aprovado',
            'statuses': statuses,
            'trps': trps
    }
    return render(request, 'locacao_acao_consulta.html', context)


def defcomprasupdumalocacao(request,pk):
    idpassado = pk
    consultacompras = Compras_Locacao.objects.get(locacao=idpassado)
    context = {
        'consultacompras': consultacompras,
    }
    return render(request, 'form_upd_compras.html', context)


