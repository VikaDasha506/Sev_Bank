from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from info_fiz.utils import get_exchange_rates_usd, get_exchange_rates_eur
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


class AboutSalaryProject(MenuMixin, TemplateView):
    template_name = 'salary_project.html'

    def get_context_data(self, **kwargs):
        # Теперь мы явно вызываем get_context_data из MenuMixin
        context = super().get_context_data(**kwargs)
        # Дополнительная логика для контекста, если необходимо
        return context


class AboutAcquiringProject(MenuMixin, TemplateView):
    template_name = 'acquiring.html'

    def get_context_data(self, **kwargs):
        # Теперь мы явно вызываем get_context_data из MenuMixin
        context = super().get_context_data(**kwargs)
        # Дополнительная логика для контекста, если необходимо
        return context


class AboutCashSettlementServices(MenuMixin, TemplateView):
    template_name = 'cash_settlement_services.html'

    def get_context_data(self, **kwargs):
        # Теперь мы явно вызываем get_context_data из MenuMixin
        context = super().get_context_data(**kwargs)
        # Дополнительная логика для контекста, если необходимо
        return context
