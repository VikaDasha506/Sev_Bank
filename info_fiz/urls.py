"""
URL configuration for anki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from anki import settings
# from cards import views
# from django.views.decorators.cache import cache_page
#
# loan_application.site.site_header = 'Управление моим сайтом'  # Текст в шапке
# loan_application.site.site_title = 'Административный сайт'  # Текст в титле
# loan_application.site.index_title = 'Добро пожаловать в панель управления' # Текст на главной странице
#

from django.urls import path
from . import views

app_name = 'info_fiz'  # Пространство имен для приложения

urlpatterns = [
    path('credit/', (views.AboutCreditView.as_view()), name='credit'),  # Информация по кредитованию физически х лиц
    path('deposits/', (views.AboutDepositView.as_view()), name='deposits'),  # Информация по депозитам
    path('cards/', (views.AboutCardsView.as_view()), name='cards'),  # Информация по картам
    path('invoices_transfers/', (views.AboutInvoicesView.as_view()), name='invoices_transfers'),
    # Информация по счетам и переводам
    path('securities/', (views.AboutSecuritiesView.as_view()), name='securities'),  # Информация по ценным бумагам
    path('credit/mortgage/', (views.AboutMortgageView.as_view()), name='mortgage'),  # Информация по ипотеке
    path('credit/credit_card/', (views.AboutCreditCardView.as_view()), name='credit_card'),  # Информация по кредитной карте
    path('credit/consumer_credit/', (views.AboutConsumerCreditView.as_view()), name='consumer_credit'),
    # Информация по потребительскоу кредиту
    path('credit/credit_holidays/', (views.AboutCreditHolidaysView.as_view()), name='credit_holidays'),
    # Информация по кредитным каникулам
    path('credit/mortgage/government_support/', (views.AboutGovernmentSupportView.as_view()), name='government_support'),
    # Информация по ипотеке с гос.поддержкой
    path('credit/mortgage/military_mortgage/', (views.AboutMilitaryMortgageView.as_view()), name='military_mortgage'),
    # Информация по военной ипотеке
    path('credit/mortgage/it_mortgage/', (views.AboutItMortgageView.as_view()), name='it_mortgage'),  # Информация по it-ипотеке
    path('credit/mortgage/family_mortgage/', (views.AboutFamilyMortgageView.as_view()), name='family_mortgage'),
    # Информация по семейной ипотеке


]
# python manage.py runserver
# python3 manage.py migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('Manina_A', 'anka506@rambler.ru', 'Manynya506')" | python3 manage.py shell