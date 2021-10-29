from django.urls import path

import core.views
from .views import IndexView, SistemaView, CreateSolicitView, ListLocacaoAcaoView, ConsultaLocacaoAcaoView, \
                   CreateSedeView, CreateLicView, CreateContrView, CreateCronoView, CreateAcaoView, CreateTipoLocView,\
                   CreateMemorialView, CreateComprasLocView, CreateTRPView, CreateOrcView, CreatePagtoView,\
                   CreateAprovView, CreateFornecView, CreateCatFornecView, CreateEndFornecView, CreateContFornecView,\
                   CreateStatusView, CreateTipoStatusView, CreateLocalView, CreateProjetoView, CreateLinguagemView,\
                   CreateTipoPagtoView, UpdPagtoView, UpdCronoView


from .views import salvatipoloc, consultalocacao

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sistema/', SistemaView.as_view(), name='sistema'),
    path('add/', core.views.CreateSolicitView.as_view(), name='add_loc'),
    path('listlocacoes/', core.views.ListLocacaoAcaoView.as_view(), name='list_loc'),
    path('<int:pk>/consultalocacao/', ConsultaLocacaoAcaoView.as_view(), name='cons_loc'),
    path('add_acao/', CreateAcaoView.as_view(), name='add_acao'),
    path('add_tipoloc/', CreateTipoLocView.as_view(), name='add_tipoloc'),
    path('add_memorial/', CreateMemorialView.as_view(), name='add_memorial'),
    path('add_comprasloc/', core.views.CreateComprasLocView.as_view(), name='add_comprasloc'),
    path('add_trp/', CreateTRPView.as_view(), name='add_trp'),
    path('add_orc/', CreateOrcView.as_view(), name='add_orc'),
    path('add_sede/', CreateSedeView.as_view(), name='add_sede'),
    path('add_lic/', CreateLicView.as_view(), name='add_lic'),
    path('add_contr/', CreateContrView.as_view(), name='add_contr'),
    path('add_pagto/', CreatePagtoView.as_view(), name='add_pagto'),
    path('add_crono/', CreateCronoView.as_view(), name='add_crono'),
    path('add_aprov/', CreateAprovView.as_view(), name='add_aprov'),
    path('add_fornec/', CreateFornecView.as_view(), name='add_fornec'),
    path('add_catfornec/', CreateCatFornecView.as_view(), name='add_catfornec'),
    path('add_endfornec/', CreateEndFornecView.as_view(), name='add_endfornec'),
    path('add_contfornec/', CreateContFornecView.as_view(), name='add_contfornec'),
    path('add_status/', CreateStatusView.as_view(), name='add_status'),
    path('add_tipostatus/', CreateTipoStatusView.as_view(), name='add_tipostatus'),
    path('add_local/', CreateLocalView.as_view(), name='add_local'),
    path('add_linguagem/', CreateLinguagemView.as_view(), name='add_linguagem'),
    path('add_projeto/', CreateProjetoView.as_view(), name='add_projeto'),
    path('add_tipopagto/', CreateTipoPagtoView.as_view(), name='add_tipopagto'),
    path('salvamemorial', core.views.salvamemorial, name='salvamemorial'),
    path('consultalocacao', core.views.consultalocacao, name='consultalocacao'),
    path('finalizarlocacao/<int:pk>', core.views.finalizarlocacao, name='finalizarlocacao'),
    path('salvatipoloc', core.views.salvatipoloc, name='salvatipoloc'),
    path('resultloc/<int:id>', core.views.resultloc, name='resultloc'),
    path('updatecompras/<int:pk>/', core.views.UpdComprasLocacaoView.as_view(), name='updatecompras'),
    path('updatesede/<int:pk>/', core.views.UpdSedeView.as_view(), name='updatesede'),
    path('updatecontrat/<int:pk>/', core.views.UpdContratView.as_view(), name='updatecontrat'),
    path('updatepagto/<int:pk>/', core.views.UpdPagtoView.as_view(), name='updatepagto'),
    path('updatecrono/<int:pk>/', core.views.UpdCronoView.as_view(), name='updatecrono'),
    path('consultaumalocacao/<int:pk>/', core.views.consultaumalocacao, name='consultaumalocacao')
]
