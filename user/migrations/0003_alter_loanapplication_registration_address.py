# Generated by Django 4.2 on 2024-06-28 19:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_loanapplication_passport_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='registration_address',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^г\\.\\s[А-ЯЁ][а-яё]+\\sул\\.\\s[А-ЯЁа-яё]+\\sд\\.\\s\\d+$')], verbose_name='Адрес регистрации'),
        ),
    ]
