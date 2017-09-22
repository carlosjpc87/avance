# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0006_auto_20170530_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia_automotriz',
            name='Marca',
            field=models.CharField(choices=[('AC', 'ACURA'), ('AU', 'AUDI'), ('BM', 'BMW'), ('CH', 'CHEVROLET'), ('CY', 'CHRYSLER'), ('FO', 'FORD'), ('GM', 'GMC'), ('HO', 'HONDA'), ('HY', 'HYUNDAI'), ('KI', 'KIA'), ('IN', 'INFINITI'), ('IZ', 'ISUZU'), ('LN', 'LINCOLN'), ('MZ', 'MAZDA'), ('MB', 'MERCEDES BENZ'), ('NI', 'NISSAN'), ('SE', 'SEAT'), ('VW', 'VOLKSWAGEN'), ('VO', 'VOLVO')], default='FO', max_length=2),
        ),
    ]
