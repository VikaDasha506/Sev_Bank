from django.urls import path
from . import views

app_name = 'info_corp'

urlpatterns = [
    # Информация по зарплатному проекту
    path('salary_project/', (views.AboutSalaryProject.as_view()), name='salary_project'),
    # Информация по Эквайрингу и СБП
    path('acquiring/', (views.AboutAcquiringProject.as_view()), name='acquiring'),
    # Информация о расчетно-кассовом обслуживании
    path('cash_settlement_services/', (views.AboutCashSettlementServices.as_view()), name='cash_settlement_services'),

]
