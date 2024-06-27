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


def main(request):
    return render(request, 'base.html')


class IndexView(MenuMixin, TemplateView):
    template_name = 'main_content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutCreditView(MenuMixin, TemplateView):
    template_name = 'credit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutDepositView(MenuMixin, TemplateView):
    template_name = 'deposits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutCardsView(MenuMixin, TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutInvoicesView(MenuMixin, TemplateView):
    template_name = 'invoices_transfers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutSecuritiesView(MenuMixin, TemplateView):
    template_name = 'accounts_securities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutMortgageView(MenuMixin, TemplateView):
    template_name = 'mortgage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutConsumerCreditView(MenuMixin, TemplateView):
    template_name = 'consumer_credit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutCreditCardView(MenuMixin, TemplateView):
    template_name = 'credit_card.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutCreditHolidaysView(MenuMixin, TemplateView):
    template_name = 'credit_holidays.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutGovernmentSupportView(MenuMixin, TemplateView):
    template_name = 'government_support.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutMilitaryMortgageView(MenuMixin, TemplateView):
    template_name = 'military_mortgage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutItMortgageView(MenuMixin, TemplateView):
    template_name = 'it_mortgage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutFamilyMortgageView(MenuMixin, TemplateView):
    template_name = 'family_mortgage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def home_usd(request):
    rates = get_exchange_rates_usd()
    return render(request, 'currency.html', {'rates': rates})


def home_eur(request):
    rates = get_exchange_rates_eur()
    return render(request, 'currency.html', {'rates': rates})
