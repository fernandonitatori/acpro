from django.urls import path
from .views import IndexView, SiteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('site/', SiteView.as_view(), name='site'),
]
