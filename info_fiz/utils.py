# Создание функции для получения курсов валют:
import requests
from django.core.exceptions import ImproperlyConfigured


def get_exchange_rates_usd():
    url = 'https://v6.exchangerate-api.com/v6/f4361dc2a5328f2fa95e64fa/latest/USD'
    params = {
        'base': 'USD',
        'symbols': 'RUB'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['conversion_rates']


def get_exchange_rates_eur():
    url = 'https://v6.exchangerate-api.com/v6/f4361dc2a5328f2fa95e64fa/latest/EUR'
    params = {
        'base': 'EUR',
        'symbols': 'RUB'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['conversion_rates']
