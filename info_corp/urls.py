from django.urls import path
from . import views

app_name = 'info_corp'  # Пространство имен для приложения

urlpatterns = [
    path('salary_project/', (views.AboutSalaryProject.as_view()), name='salary_project'),  # Информация по зарплатному проекту
    path('acquiring/', (views.AboutAcquiringProject.as_view()), name='acquiring'),  # Информация по Эквайрингу и СБП
    path('cash_settlement_services/', (views.AboutCashSettlementServices.as_view()), name='cash_settlement_services'),

]
