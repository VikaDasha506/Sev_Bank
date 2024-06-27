from django.shortcuts import render
from django.views.generic import TemplateView
from info_fiz.utils import get_exchange_rates_usd, get_exchange_rates_eur
import requests
from django.core.exceptions import ImproperlyConfigured
from datetime import datetime


class MenuMixin:
    def get_context_data(self, **kwargs):
        # Вызываем базовую реализацию для получения контекста
        context = super().get_context_data(**kwargs)
        # Получаем курсы валют и добавляем их в контекст
        rates_usd = get_exchange_rates_usd()
        rates_eur = get_exchange_rates_eur()
        context['USD'] = rates_usd
        context['EUR'] = rates_eur
        context['current_date'] = datetime.now().strftime('%d.%m.%Y')
        return context


class AboutBankView(MenuMixin, TemplateView):
    template_name = 'history.html'
    extra_context = {'title': 'О Банке'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

