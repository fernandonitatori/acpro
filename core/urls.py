from django.urls import path
from .views import IndexView, SistemaView, CreateSolicitView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sistema/', SistemaView.as_view(), name='sistema'),
    path('add/', CreateSolicitView.as_view(), name='add_loc'),
]
