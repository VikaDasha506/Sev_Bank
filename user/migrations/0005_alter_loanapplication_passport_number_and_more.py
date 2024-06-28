# Generated by Django 4.2 on 2024-06-28 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_loanapplication_passport_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='passport_number',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{6}$')], verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='passport_series',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{4}$')], verbose_name='Серия паспорта'),
        ),
    ]
