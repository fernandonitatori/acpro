from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

from .models import Locacao_Acao, Acao, TipoLocacao, Memorial, Compras_Locacao, TRP, Orcamento, Sede, Licitacao, \
                    Contrato_Locacao, Pagamento, Cronograma, Aprovacao, Fornecedor, CatFornecedor, EndFornecedor, \
                    ContFornecedor, Tipo_Status, Status, Local, Linguagem, Projeto, TipoPagto

from .forms import TipoLocacaoModelForm, MemorialModelForm, ComprasLocacaoModelForm, LocacaoAcaoModelForm, \
                   SedeModelForm,  ContratoLocacaoModelForm, PagamentoModelForm


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


class CreateSolicitView(SuccessMessageMixin, CreateView):
    model = Locacao_Acao
    template_name = 'form_solicit_loc.html'
    fields = ['tipo_locacao', 'acao', 'memorial', 'status', 'status_geral', 'descricao']
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
    fields = ['tipo_locacao', 'acao', 'memorial', 'status', 'status_geral']
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
    fields = ['descricao', 'numero', 'data', 'observacoes', 'locacao', 'trp', 'status', 'sede']
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
    fields = ['descricao', 'numero', 'dataminuta', 'datadca', 'anotacoes', 'licitacao', 'locacao', 'status']
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
              'valorlocacao', 'locacao', 'status']
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
              'tiponota', 'numnota', 'dataemissnota', 'serienota', 'xml', 'anotacoes', 'locacao', 'status']
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
    if Compras_Locacao.objects.filter(locacao=idpassado).exists():
        consultacompras = Compras_Locacao.objects.get(locacao=idpassado)
    consultasede = ''
    if Sede.objects.filter(locacao=idpassado).exists():
        consultasede = Sede.objects.get(locacao=idpassado)
    consultacontrat = ''
    if Contrato_Locacao.objects.filter(locacao=idpassado).exists():
        consultacontrat = Contrato_Locacao.objects.get(locacao=idpassado)
    consultapagto = ''
    if Pagamento.objects.filter(locacao=idpassado).exists():
        consultapagto = Pagamento.objects.get(locacao=idpassado)
    consultareceb = ''
    if Cronograma.objects.filter(locacao=idpassado).exists():
        consultareceb = Cronograma.objects.get(locacao=idpassado)
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
            'memoriais': memoriais
    }
    return render(request, 'locacao_acao_consulta.html', context)


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
              'tiponota', 'numnota', 'dataemissnota', 'serienota', 'xml', 'anotacoes', 'status']
    success_url = reverse_lazy('list_loc')
    context_object_name = 'consultapagto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Processo em Pagamento cadastrado com sucesso!"

    def post(self, request, *args, **kwargs):
        form = PagamentoModelForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locacao']
            print(loc)
            locacao = Locacao_Acao.objects.get(descricao = loc)
            locacao.status_geral = form.cleaned_data['status']
            locacao.save()
            super(UpdPagtotView, self).post(request, **kwargs)
            messages.success(request, 'Processo em Pagamento atualizado com sucesso')
            return HttpResponseRedirect(reverse_lazy('consultaumalocacao', args=[locacao.id]))
        return render(request, 'resultado.html', {'form': form})


def resultloc(request, id):
    idpassado = id
    context = {
        'id': idpassado,
    }
    return render(request, 'resultado.html', context)
