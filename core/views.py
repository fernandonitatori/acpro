from django.views.generic import TemplateView


class IndexView(TemplateView):
        template_name = 'index.html'


class SiteView(TemplateView):
    template_name = 'site.html'
