from typing import Any
from django.shortcuts import render
from django.views import generic
from . import models


class IndexView(generic.TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        welcome = models.TextInformation.objects.get(id=1)
        learning = models.TextInformation.objects.get(id=2)
        context['welcome'] = welcome.text
        context['learning'] = learning.text
        context['certificates'] = models.Certificate.objects.all().order_by('date')
        return context


class WorksView(generic.TemplateView):
    template_name = 'portfolio/works.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = models.ProjectInformation.objects.all().order_by('-date')
        return context
    

class ContactView(generic.TemplateView):
    template_name = 'portfolio/contacts.html'