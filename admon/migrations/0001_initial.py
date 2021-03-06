# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comercial', '0002_auto_20170505_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta_Bancaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banco', models.CharField(choices=[('bv', 'BBVA'), ('cb', 'Citi Banamex'), ('bn', 'Banorte'), ('st', 'Santander'), ('hs', 'HSBC'), ('in', 'Inbursa'), ('br', 'Ban Regio'), ('bb', 'Ban Bajio')], default='bv', max_length=2)),
                ('Sucursal', models.CharField(blank=True, max_length=10, null=True)),
                ('Num_Cuenta', models.PositiveIntegerField(blank=True, null=True)),
                ('Clave_Interbancaria', models.PositiveIntegerField(blank=True, null=True)),
                ('Agencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comercial.Agencia_Automotriz')),
                ('Contacto_Agencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comercial.Contacto_Agencia')),
            ],
        ),
    ]
