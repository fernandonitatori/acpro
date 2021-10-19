from django.urls import path

import core.views
from .views import IndexView, SistemaView, CreateSolicitView, ListLocacaoAcaoView, ConsultaLocacaoAcaoView
from .views import ListUpdLocacaoAcaoView, CreateAcaoView, CreateTipoLocView, CreateMemorialView, CreateComprasLocView
from core.views import salvatipoloc

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sistema/', SistemaView.as_view(), name='sistema'),
    path('add/', core.views.CreateSolicitView.as_view(), name='add_loc'),
    path('listlocacoes/', ListLocacaoAcaoView.as_view(), name='list_loc'),
    path('<int:pk>/consultalocacao/', ConsultaLocacaoAcaoView.as_view(), name='cons_loc'),
    path('listupdlocacoes/', ListUpdLocacaoAcaoView.as_view(), name='list_upd_loc'),
    path('add_acao/', CreateAcaoView.as_view(), name='add_acao'),
    path('add_tipoloc/', CreateTipoLocView.as_view(), name='add_tipoloc'),
    path('add_memorial/', CreateMemorialView.as_view(), name='add_memorial'),
    path('add_comprasloc/', CreateComprasLocView.as_view(), name='add_comprasloc'),
    path('salvatipoloc', core.views.salvatipoloc, name='salvatipoloc')
]
