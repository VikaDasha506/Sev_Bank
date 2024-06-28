from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # Обратная звязь
    path('feedback/', (views.FeedBack.as_view()), name='feedback'),
    # Благодарность за обратную звязь
    path('feedback/thanks/', (views.ThanksForFeedback.as_view()), name='thanks'),
    # Кредитный калькулятор
    path('customer/', (views.CustomerCreate.as_view()), name='calculator'),
    # Результат расчета калькулятора
    path('customer/result', (views.CustomerResult.as_view()), name='result'),
    # Сохранение результатов расчета
    path('save_loan_data/', views.save_loan_data, name='loan_data'),
    # Заявка на кредит
    path('customer/loan_applications/', (views.CustomerLoanApplications.as_view()), name='customer_loan_application'),
    # Благодарность за отправленную заявку
    path('customer/loan_application_success/', (views.LoanApplicationSuccess.as_view()),
         name='loan_application_success'),
]
