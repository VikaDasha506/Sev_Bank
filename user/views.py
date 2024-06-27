from django.shortcuts import render
from .models import Feedback, Calculator, LoanApplication, Loan
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.decorators.csrf import csrf_protect
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


class FeedBack(MenuMixin, CreateView):
    model = Feedback
    template_name = 'feedback.html'
    redirect_field_name = 'next'
    success_url = reverse_lazy('user:thanks')
    fields = ['name', 'email', 'message']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class ThanksForFeedback(MenuMixin, TemplateView):
    template_name = 'feedback_thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@csrf_protect
def save_loan_data(request):
    if request.method == 'POST':
        # Получаем данные из запроса
        amount = request.POST.get('amount')
        term = request.POST.get('term')
        interest_rate = request.POST.get('interestRate')
        monthly_payment = request.POST.get('monthlyPayment')
        total_payment = request.POST.get('totalPayment')
        total_interest = request.POST.get('totalInterest')
        # Создаем новый объект Loan и сохраняем данные
        loan = Loan(
            amount=amount,
            term=term,
            interest_rate=interest_rate,
            monthly_payment=monthly_payment,
            total_payment=total_payment,
            total_interest=total_interest
        )
        loan.save()
        # Сохраняем ID расчета кредита в сессии
        request.session['loan_id'] = loan.id

        return render(request, 'result.html', {'loanData': loan})
    else:
        return render(request, 'error_page.html', {'message': 'Invalid request'})


class CustomerCreate(MenuMixin, CreateView):
    model = Calculator
    template_name = 'calculator.html'
    fields = ['amount', 'term', 'interest_rate', 'monthly_payment', 'total_payment', 'total_interest']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomerResult(MenuMixin, TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomerLoanApplications(MenuMixin, CreateView):
    model = LoanApplication
    template_name = 'loan_application.html'
    fields = ['name', 'last_name', 'patronymic', 'date_birth', 'passport_series', 'passport_number',
              'registration_address', 'email']
    redirect_field_name = 'next'
    success_url = reverse_lazy('user:loan_application_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        # Получаем ID расчета кредита из сессии
        loan_id = self.request.session.get('loan_id')
        if loan_id:
            loan = Loan.objects.get(id=loan_id)
            form.instance.customer = loan
            return super().form_valid(form)
        else:
            form.add_error(None, 'Loan calculation not found')
            return self.form_invalid(form)


class LoanApplicationSuccess(MenuMixin, TemplateView):
    template_name = 'loan_application_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
