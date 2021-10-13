from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Locacao_Acao

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
    fields = ['tipo_locacao', 'acao', 'memorial', 'descricao','status']
    success_url = reverse_lazy('sistema')