from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Locacao_Acao

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
    fields = ['tipo_locacao','acao','memorial','status']
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
