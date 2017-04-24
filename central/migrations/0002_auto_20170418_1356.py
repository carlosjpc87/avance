# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-18 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0008_auto_20170418_0205'),
        ('central', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentacion_pmoral',
            old_name='Para_Anexo',
            new_name='Anexo',
        ),
        migrations.RenameField(
            model_name='documentacion_pmoral',
            old_name='Para_Contrato',
            new_name='Contrato',
        ),
        migrations.RenameField(
            model_name='documentacion_pmoral',
            old_name='En_Fecha',
            new_name='Fecha',
        ),
        migrations.AddField(
            model_name='documentacion_pmoral',
            name='Caso',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='comercial.Caso'),
            preserve_default=False,
        ),
    ]