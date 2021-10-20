from django.urls import path

import core.views
from .views import IndexView, SistemaView, CreateSolicitView, ListLocacaoAcaoView, ConsultaLocacaoAcaoView, \
                   CreateDCAView, CreateLicView, CreateContrView, CreateCronoView
from .views import ListUpdLocacaoAcaoView, CreateAcaoView, CreateTipoLocView, CreateMemorialView, CreateComprasLocView,\
                   CreateTRPView, CreateOrcView, CreatePagtoView, CreateAprovView, CreateFornecView,\
                   CreateCatFornecView, CreateEndFornecView, CreateContFornecView, CreateStatusView,\
                   CreateTipoStatusView, CreateLocalView, CreateProjetoView, CreateLinguagemView, CreateTipoPagtoView
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
    path('add_trp/', CreateTRPView.as_view(), name='add_trp'),
    path('add_orc/', CreateOrcView.as_view(), name='add_orc'),
    path('add_dca/', CreateDCAView.as_view(), name='add_dca'),
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
    path('salvatipoloc', core.views.salvamemorial, name='salvamemorial'),
    path('salvatipoloc', core.views.salvatipoloc, name='salvatipoloc')
]
