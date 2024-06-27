# Создание функции для получения курсов валют:
import requests
from django.core.exceptions import ImproperlyConfigured


def get_exchange_rates_usd():
    url = 'https://v6.exchangerate-api.com/v6/c39ba5fc361ff2f7cda3b7b9/latest/USD'
    params = {
        'base': 'USD',
        'symbols': 'RUB'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['conversion_rates']


def get_exchange_rates_eur():
    url = 'https://v6.exchangerate-api.com/v6/c39ba5fc361ff2f7cda3b7b9/latest/EUR'
    params = {
        'base': 'EUR',
        'symbols': 'RUB'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['conversion_rates']
