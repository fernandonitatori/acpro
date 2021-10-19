from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Locacao_Acao, Acao, TipoLocacao, Memorial, Compras_Locacao
from .forms import TipoLocacaoModelForm


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


def salvatipoloc(request):
    descricao = request.POST.get('descricao')
    if (TipoLocacao.objects.filter(descricao=descricao).exists()):
        messages.error(request, "Tipo de locação já cadastrado!")
        return redirect('../add/')
    else:
        form = TipoLocacaoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../add/')

