from django.urls import path
from .views import IndexView, SistemaView, CreateSolicitView, ListLocacaoAcaoView, ConsultaLocacaoAcaoView, ListUpdLocacaoAcaoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sistema/', SistemaView.as_view(), name='sistema'),
    path('add/', CreateSolicitView.as_view(), name='add_loc'),
    path('listlocacoes/', ListLocacaoAcaoView.as_view(), name='list_loc'),
    path('<int:pk>/consultalocacao/',ConsultaLocacaoAcaoView.as_view(), name='cons_loc'),
    path('listupdlocacoes/', ListUpdLocacaoAcaoView.as_view(), name='list_upd_loc')
]
