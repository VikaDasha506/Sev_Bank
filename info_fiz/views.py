from django.shortcuts import render
from django.views.generic import TemplateView
from info_fiz.utils import get_exchange_rates_usd, get_exchange_rates_eur
import requests
from django.core.exceptions import ImproperlyConfigured


def main(request):
    return render(request, 'base.html')


class AboutFizView(TemplateView):
    template_name = 'face_fiz.html'
    extra_context = {'title': 'О кредитах'}


class IndexView(TemplateView):
    """наследует TemplateView.
     Oсновная страница. Шаблон 'main.html'."""
    template_name = 'main_content.html'


def get_credit(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'credit.html')


def get_deposits(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'deposits.html')


def get_cards(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'cards.html')


def get_invoices_transfers(request):
    return render(request, 'invoices_transfers.html')


def get_securities(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'accounts_securities.html')


def get_additional_services(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'additional_services.html')


def get_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'mortgage.html')


def get_consumer_credit(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'consumer_credit.html')


def get_credit_card(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'credit_card.html')


def get_credit_holidays(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'credit_holidays.html')


def get_government_support(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'government_support.html')


def get_military_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'military_mortgage.html')


def get_it_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'it_mortgage.html')


def get_family_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'family_mortgage.html')


def home_usd(request):
    rates = get_exchange_rates_usd()
    return render(request, 'currency.html', {'rates': rates})


def home_eur(request):
    rates = get_exchange_rates_eur()
    return render(request, 'currency.html', {'rates': rates})


class HomeView(IndexView):
    """ Класс, который наследует от IndexView,
        и переопределяет метод get_context_data(),
        чтобы вернуть данные о курсах валют. """
    template_name = 'main_content.html'

    def get_context_data(self, **kwargs):
        # Вызываем базовую реализацию для получения контекста
        context = super().get_context_data(**kwargs)
        # Получаем курсы валют и добавляем их в контекст
        rates_usd = get_exchange_rates_usd()
        rates_eur = get_exchange_rates_eur()
        context['USD'] = rates_usd
        context['EUR'] = rates_eur
        return context
