from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, EmailValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import date


class Feedback(models.Model):  # Модель обратной связи
    class Status(models.IntegerChoices):
        UNCHECKED = 0, 'Не проверено'
        CHECKED = 1, 'Проверено'

    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(blank=False, null=False, verbose_name='email')
    message = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Сообщение')
    check_status = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]),
                                                         Status.choices)), default=Status.UNCHECKED,
                                       verbose_name='Статус проверки')

    def __str__(self):
        return f'{self.name} - {self.email} - {self.message}'


class Calculator(models.Model):  # Модель кредитного калькулятора
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 validators=[MinValueValidator(100000), MaxValueValidator(5000000)])
    term = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])  # срок
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2,
                                        validators=[MinValueValidator(0), MaxValueValidator(100)])  # процентная ставка
    monthly_payment = models.CharField(max_length=255)
    total_payment = models.CharField(max_length=255)
    total_interest = models.CharField(max_length=255)


class Loan(models.Model):  # Модель результата расчета
    amount = models.CharField(max_length=255)  # сумма
    term = models.CharField(max_length=255)  # срок
    interest_rate = models.CharField(max_length=255)  # процентная ставка
    monthly_payment = models.CharField(max_length=255)
    total_payment = models.CharField(max_length=255)
    total_interest = models.CharField(max_length=255)

    def __str__(self):
        return f'сумма:{self.amount}, срок:{self.term}, ставка:{self.interest_rate} %'


class LoanApplication(models.Model):  # Модель кредитной заявки
    customer = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name='Расчеты калькулятора')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    date_birth = models.DateField(verbose_name='Дата рождения')
    passport_series = models.CharField(
        max_length=4,
        validators=[RegexValidator(
            r'^\d{4}$', message=_('Введите корректную серию паспорта.'))
        ],
        verbose_name='Серия паспорта'
    )
    passport_number = models.CharField(
        max_length=6,
        validators=[RegexValidator(
            r'^\d{6}$', message=_('Введите корректный номер паспорта.'))
        ],
        verbose_name='Номер паспорта'
    )
    registration_address = models.CharField(max_length=255,
                                            validators=[RegexValidator(
                                                r'^г\.?\s*[А-ЯЁ][а-яё]+\s*,?\s*ул\.?\s*[А-ЯЁа-яё0-9]+\s*,?\s*д\.?\s*\d+',
                                                message=_('формат ввода: г. ул. д.'))],
                                            verbose_name='Адрес регистрации')
    email = models.EmailField(validators=[EmailValidator()],
                              verbose_name='Адрес электронной почты')

    def clean(self):
        super().clean()
        age = self.calculate_age(self.date_birth)
        if age < 21:
            raise ValidationError({
                'date_birth': _('Возраст должен быть не меньше 21 года.')
            })
        elif age > 65:
            raise ValidationError({
                'date_birth': _('Возраст не может превышать 65 лет.')
            })

    @staticmethod
    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return (f'{self.patronymic}-{self.name} - {self.last_name}- {self.date_birth}- {self.passport_series}-'
                f' {self.passport_number}- {self.registration_address}- {self.email}')
