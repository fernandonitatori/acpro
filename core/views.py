from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from datetime import *
from dateutil.relativedelta import relativedelta

from .models import Locacao_Acao, Acao, TipoLocacao, Memorial, Compras_Locacao, TRP, Orcamento, Sede, Licitacao, \
                    Contrato_Locacao, Pagamento, Cronograma, Aprovacao, Fornecedor, CatFornecedor, EndFornecedor, \
                    ContFornecedor, Tipo_Status, Status, Local, Linguagem, Projeto, TipoPagto

from .forms import TipoLocacaoModelForm, MemorialModelForm, ComprasLocacaoModelForm, LocacaoAcaoModelForm, \
                   SedeModelForm,  ContratoLocacaoModelForm, PagamentoModelForm, CronogramaModelForm


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
        compras = Compras_Locacao.objects.all()
        countcompras = 0
        for compra in compras:
            if not str(compra.status) == 'Compras - Aprovado':
                countcompras += 1
                print(countcompras)

        sedes = Sede.objects.all()
        countsede = 0
        for sede in sedes:
            if not str(sede.status) == 'Sede - Aprovado':
                countsede += 1
                print(countsede)

        contratos = Contrato_Locacao.objects.all()
        countcontr = 0
        for contrato in contratos:
            if not str(contrato.status) == 'Contratação - Aprovado':
                countcontr += 1
                print(countcontr)

        pagtos = Pagamento.objects.all()
        countpagto = 0
        for pagto in pagtos:
            if not str(pagto.status) == 'Pagamento - Aprovado':
                countpagto += 1
                print(countpagto)

        cronos = Cronograma.objects.all()
        countcrono = 0
        for crono in cronos:
            if not str(crono.status) == 'Recebimento - Aprovado':
                countcrono += 1
                print(countcrono)

        countfin = 0
        locs = Locacao_Acao.objects.all()
        for loc in locs:
            if str(loc.status_geral) == 'Finalizado':
                countfin += 1

        context['numcompras'] = countcompras
        context['numsede'] = countsede
        context['numcontr'] = countcontr
        context['numpagto'] = countpagto
        context['numrec'] = countcrono
        context['numfin'] = countfin

        return context


class CreateSolicitView(SuccessMessageMixin, CreateView):
    model = Locacao_Acao
    template_name = 'form_solicit_loc.html'
    fields = ['tipo_locacao', 'acao', 'memorial', 'prazo', 'status', 'status_geral', 'descricao']
    success_url = reverse_lazy('add_loc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tiposlocacao'] = TipoLocacao.objects.all()
        context['acoes'] = Acao.objects.all()
        context['memoriais'] = Memorial.objects.all()
        context['statuses'] = Status.objects.all()
        context['projetos'] = Projeto.objects.all()
        context['linguagens'] = Linguagem.objects.all()
        context['locais'] = Local.objects.all()
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Solicitação cadastrada com sucesso!"



class ConsultaLocacaoAcaoView(UpdateView):
    model = Locacao_Acao
    template_name = 'locacao_acao_consulta.html'
    fields = ['tipo_locacao', 'acao', 'memorial', 'prazo', 'status', 'status_geral']
    context_object_name = 'consulta'
    success_url = reverse_lazy('sistema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_chave_sol'] = 'Solicitado'
        context['tiposlocacao'] = TipoLocacao.objects.all()
        context['acoes'] = Acao.objects.all()
        context['memoriais'] = Memorial.objects.all()
        context['statuses'] = Status.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = LocacaoAcaoModelForm(request.POST)
        if form.is_valid():
            loc = self.kwargs.get("pk")
            print(loc)
            super(ConsultaLocacaoAcaoView, self).post(request, **kwargs)
            messages.success(request, 'Processo em Solicitação atualizado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[loc]))
        return render(request, 'resultado.html', {'form': form})


class ListUpdLocacaoAcaoView(ListView):
    model = Locacao_Acao
    template_name = 'locacao_acao_updlistview.html'
    queryset = Locacao_Acao.objects.all()
    context_object_name = 'updlocacoes'


class CreateAcaoView(SuccessMessageMixin, CreateView):
    model = Acao
    template_name = 'form_solicit_loc.html'
    fields = ['nome', 'descricao', 'observacoes', 'data_base', 'projeto', 'linguagem', 'local']
    success_url = reverse_lazy('add_loc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['linguagens'] = Linguagem.objects.all()
        context['locais'] = Local.objects.all()
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Ação cadastrada com sucesso!"

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


class CreateComprasLocView(SuccessMessageMixin, CreateView):
    model = Compras_Locacao
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'numero', 'data', 'observacoes', 'locacao', 'trp', 'prazo', 'status', 'sede']
    success_url = reverse_lazy('list_loc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trps'] = TRP.objects.all()
        context['statuses'] = Status.objects.all()
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Compras cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = ComprasLocacaoModelForm(request.POST)
        if form.is_valid():
            compra = form.save()
            print(compra.locacao)
            locacao = Locacao_Acao.objects.get(descricao = compra.locacao)
            locacao.status_geral = compra.status
            print(locacao)
            print(compra.status)
            locacao.save()
            compra.save()
            messages.success(request, 'Processo em compras cadastrado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


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


class CreateSedeView(SuccessMessageMixin, CreateView):
    model = Sede
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'numero', 'dataminuta', 'datadca', 'anotacoes', 'licitacao', 'locacao', 'prazo',  'status']
    success_url = reverse_lazy('list_loc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Sede cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = SedeModelForm(request.POST)
        if form.is_valid():
            sede = form.save()
            print(sede.locacao)
            locacao = Locacao_Acao.objects.get(descricao = sede.locacao)
            locacao.status_geral = sede.status
            print(locacao)
            print(sede.status)
            locacao.save()
            sede.save()
            messages.success(request, 'Processo em Sede cadastrado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


class CreateLicView(CreateView):
    model = Licitacao
    template_name = 'form_create_lic.html'
    fields = ['dataabertura', 'datapregao', 'dataassinatura', 'datahomologacao', 'vencedor', 'valor']
    success_url = reverse_lazy('sistema')


class CreateContrView(CreateView, SuccessMessageMixin):
    model = Contrato_Locacao
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'processo', 'dataprocesso', 'instrcontratual', 'datacontrato', 'valorservico',
              'valorlocacao', 'locacao', 'prazo', 'status']
    success_url = reverse_lazy('sistema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Contratação cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = ContratoLocacaoModelForm(request.POST)
        if form.is_valid():
            contrato = form.save()
            print(contrato.locacao)
            locacao = Locacao_Acao.objects.get(descricao = contrato.locacao)
            locacao.status_geral = contrato.status
            print(locacao)
            print(contrato.status)
            locacao.save()
            contrato.save()
            messages.success(request, 'Processo em Contratação cadastrado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


class CreatePagtoView(CreateView, SuccessMessageMixin):
    model = Pagamento
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'tipo_pagto', 'atividade', 'parcela', 'qtde_parcelas', 'valor', 'dataprevnota',
              'tiponota', 'numnota', 'dataemissnota', 'serienota', 'xml', 'anotacoes', 'locacao', 'prazo', 'status']
    success_url = reverse_lazy('list_loc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Pagamento cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = PagamentoModelForm(request.POST)
        if form.is_valid():
            pagto = form.save()
            print(pagto.locacao)
            locacao = Locacao_Acao.objects.get(descricao = pagto.locacao)
            locacao.status_geral = pagto.status
            print(locacao)
            print(pagto.status)
            locacao.save()
            pagto.save()
            messages.success(request, 'Processo em Contratação cadastrado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


class CreateCronoView(CreateView):
    model = Cronograma
    template_name = 'locacao_acao_consulta.html'
    fields = ['locacao', 'atividade', 'datainicio', 'datafim', 'anotacoes', 'prazo', 'status']
    success_url = reverse_lazy('list_loc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Recebimento cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = CronogramaModelForm(request.POST)
        if form.is_valid():
            crono = form.save()
            print(crono.locacao)
            locacao = Locacao_Acao.objects.get(descricao = crono.locacao)
            locacao.status_geral = crono.status
            print(locacao)
            print(crono.status)
            locacao.save()
            crono.save()
            messages.success(request, 'Processo em Recebimento cadastrado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


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
        messages.error(request, 'Tipo de locação já cadastrada', extra_tags='tipoloc')
        return redirect('../add/')
    else:
        form = TipoLocacaoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de locação incluída com sucesso', extra_tags='tipoloc')
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
            messages.success(request, 'Memorial Cadastrado com sucesso')
            return redirect('../add/')


def consultalocacao(request):
    tipoloc = request.POST.get("tipo_locacao")
    acao = request.POST.get("acao")
    memorial = request.POST.get("memorial")
    status_geral = request.POST.get("status_geral")
    print(request.POST)

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
    if status_geral != '':
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
        locacoes = Locacao_Acao.objects.filter(status_geral=status_geral)
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
    consulta = get_object_or_404(Locacao_Acao,id=pk)
    consultacompras = ''
    dataprazocompras = ''
    dataprazo1compras = ''
    dataprazo2compras = ''
    if Compras_Locacao.objects.filter(locacao=idpassado).exists():
        consultacompras = Compras_Locacao.objects.get(locacao=idpassado)
        dataprazocompras = consultacompras.criado + relativedelta(days=consultacompras.prazo)
        dataprazo1compras = consultacompras.criado + relativedelta(days=(consultacompras.prazo/3))
        dataprazo2compras = dataprazo1compras + relativedelta(days=(consultacompras.prazo/3))
        dataprazocompras = dataprazocompras.date()
        dataprazo1compras = dataprazo1compras.date()
        dataprazo2compras = dataprazo2compras.date()

    consultasede = ''
    dataprazosede = ''
    dataprazo1sede = ''
    dataprazo2sede = ''
    if Sede.objects.filter(locacao=idpassado).exists():
        consultasede = Sede.objects.get(locacao=idpassado)
        dataprazosede = consultasede.criado + relativedelta(days=consultasede.prazo)
        dataprazo1sede = consultasede.criado + relativedelta(days=(consultasede.prazo / 3))
        dataprazo2sede = dataprazo1sede + relativedelta(days=(consultasede.prazo / 3))
        dataprazosede = dataprazosede.date()
        dataprazo1sede = dataprazo1sede.date()
        dataprazo2sede = dataprazo2sede.date()

    consultacontrat = ''
    dataprazocontrat = ''
    dataprazo1contrat = ''
    dataprazo2contrat = ''

    if Contrato_Locacao.objects.filter(locacao=idpassado).exists():
        consultacontrat = Contrato_Locacao.objects.get(locacao=idpassado)
        dataprazocontrat = consultacontrat.criado + relativedelta(days=consultacontrat.prazo)
        dataprazo1contrat = consultacontrat.criado + relativedelta(days=(consultacontrat.prazo / 3))
        dataprazo2contrat = dataprazo1contrat + relativedelta(days=(consultacontrat.prazo / 3))
        dataprazocontrat = dataprazocontrat.date()
        dataprazo1contrat = dataprazo1contrat.date()
        dataprazo2contrat = dataprazo2contrat.date()

    consultapagto = ''
    dataprazopagto = ''
    dataprazo1pagto = ''
    dataprazo2pagto = ''
    if Pagamento.objects.filter(locacao=idpassado).exists():
        consultapagto = Pagamento.objects.get(locacao=idpassado)
        dataprazopagto = consultapagto.criado + relativedelta(days=consultapagto.prazo)
        dataprazo1pagto = consultapagto.criado + relativedelta(days=(consultapagto.prazo / 3))
        dataprazo2pagto = dataprazo1pagto + relativedelta(days=(consultapagto.prazo / 3))
        dataprazopagto = dataprazopagto.date()
        dataprazo1pagto = dataprazo1pagto.date()
        dataprazo2pagto = dataprazo2pagto.date()

    consultareceb = ''
    dataprazoreceb = ''
    dataprazo1receb = ''
    dataprazo2receb = ''
    if Cronograma.objects.filter(locacao=idpassado).exists():
        consultareceb = Cronograma.objects.get(locacao=idpassado)
        dataprazoreceb = consultareceb.criado + relativedelta(days=consultareceb.prazo)
        dataprazo1receb = consultareceb.criado + relativedelta(days=(consultareceb.prazo / 3))
        dataprazo2receb = dataprazo1receb + relativedelta(days=(consultareceb.prazo / 3))
        dataprazoreceb = dataprazoreceb.date()
        dataprazo1receb = dataprazo1receb.date()
        dataprazo2receb = dataprazo2receb.date()

    datahoje = date.today()
    statuses = Status.objects.all()
    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    trps = TRP.objects.all()
    licitacoes = Licitacao.objects.all()
    pagamentos = Pagamento.objects.all()
    tipospagto = TipoPagto.objects.all()
    context = {
            'consulta': consulta,
            'consultacompras': consultacompras,
            'consultasede': consultasede,
            'consultacontrat': consultacontrat,
            'consultapagto': consultapagto,
            'consultareceb': consultareceb,
            'status_chave_sol': 'Solicitado',
            'status_chave_compras': 'Compras - Aprovado',
            'status_chave_sede': 'Sede - Aprovado',
            'status_chave_contrat': 'Contratação - Aprovado',
            'status_chave_pagto': 'Pagamento - Aprovado',
            'status_chave_receb': 'Recebimento - Aprovado',
            'statuses': statuses,
            'trps': trps,
            'tiposlocacao': tiposlocacao,
            'acoes': acoes,
            'licitacoes': licitacoes,
            'pagamentos': pagamentos,
            'tipospagto': tipospagto,
            'memoriais': memoriais,
            'datahoje': datahoje,
            'dataprazocompras': dataprazocompras,
            'dataprazo1compras': dataprazo1compras,
            'dataprazo2compras': dataprazo2compras,
            'dataprazosede': dataprazosede,
            'dataprazo1sede': dataprazo1sede,
            'dataprazo2sede': dataprazo2sede,
            'dataprazocontrat': dataprazocontrat,
            'dataprazo1contrat': dataprazo1contrat,
            'dataprazo2contrat': dataprazo2contrat,
            'dataprazopagto': dataprazopagto,
            'dataprazo1pagto': dataprazo1pagto,
            'dataprazo2pagto': dataprazo2pagto,
            'dataprazoreceb': dataprazoreceb,
            'dataprazo1receb': dataprazo1receb,
            'dataprazo2receb': dataprazo2receb
    }
    return render(request, 'locacao_acao_consulta.html', context)


def finalizarlocacao(request,pk):
    idpassado = pk
    consulta = Locacao_Acao.objects.get(id=idpassado)
    statusfinal = Status.objects.get(descricao='Finalizado')
    print(statusfinal)
    consulta.status_geral = statusfinal
    consulta.save()
    messages.success(request, 'Processo  de locação finalizado com sucesso!')
    return redirect('consultaumalocacao',pk=idpassado)


def listloc_compras(request):
    locacoes_compras = Locacao_Acao.objects.filter(status_geral__descricao__startswith='Compras')
    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    statuses = Status.objects.all()

    context = {
        'locacoes': locacoes_compras,
        'tiposlocacao': tiposlocacao,
        'acoes': acoes,
        'memoriais': memoriais,
        'statuses': statuses
    }
    return render(request, 'locacao_acao_listview.html', context)


def listloc_sede(request):
    locacoes_sede = Locacao_Acao.objects.filter(status_geral__descricao__startswith='Sede')
    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    statuses = Status.objects.all()

    context = {
        'locacoes': locacoes_sede,
        'tiposlocacao': tiposlocacao,
        'acoes': acoes,
        'memoriais': memoriais,
        'statuses': statuses
    }
    return render(request, 'locacao_acao_listview.html', context)


def listloc_contr(request):
    locacoes_contr = Locacao_Acao.objects.filter(status_geral__descricao__startswith='Contratação')
    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    statuses = Status.objects.all()

    context = {
        'locacoes': locacoes_contr,
        'tiposlocacao': tiposlocacao,
        'acoes': acoes,
        'memoriais': memoriais,
        'statuses': statuses
    }
    return render(request, 'locacao_acao_listview.html', context)


def listloc_pagto(request):
    locacoes_pagto = Locacao_Acao.objects.filter(status_geral__descricao__startswith='Pagamento')
    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    statuses = Status.objects.all()

    context = {
        'locacoes': locacoes_pagto,
        'tiposlocacao': tiposlocacao,
        'acoes': acoes,
        'memoriais': memoriais,
        'statuses': statuses
    }
    return render(request, 'locacao_acao_listview.html', context)

def listloc_crono(request):
    locacoes_crono = Locacao_Acao.objects.filter(status_geral__descricao__startswith='Recebimento')
    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    statuses = Status.objects.all()

    context = {
        'locacoes': locacoes_crono,
        'tiposlocacao': tiposlocacao,
        'acoes': acoes,
        'memoriais': memoriais,
        'statuses': statuses
    }
    return render(request, 'locacao_acao_listview.html', context)

def listloc_fin(request):
    locacoes_fin = Locacao_Acao.objects.filter(status_geral__descricao__startswith='Finalizado')
    tiposlocacao = TipoLocacao.objects.all()
    acoes = Acao.objects.all()
    memoriais = Memorial.objects.all()
    statuses = Status.objects.all()

    context = {
        'locacoes': locacoes_fin,
        'tiposlocacao': tiposlocacao,
        'acoes': acoes,
        'memoriais': memoriais,
        'statuses': statuses
    }
    return render(request, 'locacao_acao_listview.html', context)


def defcomprasupdumalocacao(request,pk):
    idpassado = pk
    consultacompras = Compras_Locacao.objects.get(locacao=idpassado)
    context = {
        'consultacompras': consultacompras,
    }
    return render(request, 'form_upd_compras.html', context)


class UpdComprasLocacaoView(UpdateView):
    model = Compras_Locacao
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'numero', 'data', 'observacoes', 'locacao', 'trp', 'status', 'sede']
    context_object_name = 'consultacompras'
    success_url =  reverse_lazy('list_loc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_chave_sol'] = 'Solicitado'
        context['status_compras_emaprov'] = 'Compras - Em Aprovação'
        context['status_compras_emorc'] = 'Compras - Aguardando orçamento'
        context['status_compras_orc'] = 'Compras - Orçado'
        return context

    def post(self, request, *args, **kwargs):
        form = ComprasLocacaoModelForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locacao']
            print(loc)
            locacao = Locacao_Acao.objects.get(descricao = loc)
            locacao.status_geral = form.cleaned_data['status']
            locacao.save()
            super(UpdComprasLocacaoView, self).post(request, **kwargs)
            messages.success(request, 'Processo em compras atualizado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


class UpdSedeView(UpdateView):
    model = Sede
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'numero', 'dataminuta', 'datadca', 'anotacoes', 'licitacao', 'locacao', 'status']
    success_url = reverse_lazy('list_loc')
    context_object_name = 'consultasede'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Sede cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = SedeModelForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locacao']
            print(loc)
            locacao = Locacao_Acao.objects.get(descricao = loc)
            locacao.status_geral = form.cleaned_data['status']
            locacao.save()
            super(UpdSedeView, self).post(request, **kwargs)
            messages.success(request, 'Processo em Sede atualizado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


class UpdContratView(UpdateView):
    model = Contrato_Locacao
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'processo', 'dataprocesso', 'instrcontratual', 'datacontrato', 'valorservico',
                   'valorlocacao', 'locacao', 'status']
    success_url = reverse_lazy('list_loc')
    context_object_name = 'consultacontrat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Contratação cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = ContratoLocacaoModelForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locacao']
            print(loc)
            locacao = Locacao_Acao.objects.get(descricao = loc)
            locacao.status_geral = form.cleaned_data['status']
            locacao.save()
            super(UpdContratView, self).post(request, **kwargs)
            messages.success(request, 'Processo em Contratação atualizado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


class UpdPagtoView(UpdateView):
    model = Pagamento
    template_name = 'locacao_acao_consulta.html'
    fields = ['descricao', 'tipo_pagto', 'atividade', 'parcela', 'qtde_parcelas', 'valor', 'dataprevnota',
              'tiponota', 'numnota', 'dataemissnota', 'serienota', 'xml', 'anotacoes', 'locacao', 'status']
    success_url = reverse_lazy('list_loc')
    context_object_name = 'consultapagto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Pagamento atualizado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = PagamentoModelForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locacao']
            print(loc)
            locacao = Locacao_Acao.objects.get(descricao = loc)
            locacao.status_geral = form.cleaned_data['status']
            locacao.save()
            super(UpdPagtoView, self).post(request, **kwargs)
            messages.success(request, 'Processo em Pagamento atualizado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


class UpdCronoView(UpdateView):
    model = Cronograma
    fields = ['locacao', 'atividade', 'datainicio', 'datafim', 'anotacoes', 'status']
    template_name = 'locacao_acao_consulta.html'
    success_url = reverse_lazy('list_loc')
    context_object_name = 'consultareceb'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Recebimento atualizado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = CronogramaModelForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locacao']
            print(loc)
            locacao = Locacao_Acao.objects.get(descricao = loc)
            locacao.status_geral = form.cleaned_data['status']
            locacao.save()
            super(UpdCronoView, self).post(request, **kwargs)
            messages.success(request, 'Processo em Recebimento atualizado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


def resultloc(request, id):
    idpassado = id
    context = {
        'id': idpassado,
    }
    return render(request, 'resultado.html', context)
