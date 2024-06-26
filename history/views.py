from django.shortcuts import render
from django.views.generic import TemplateView


class AboutBankView(TemplateView):
    template_name = 'history.html'
    extra_context = {'title': 'О Банке'}
