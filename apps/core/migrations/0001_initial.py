# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('first_name', models.CharField(max_length=100, verbose_name='nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='sobre nome')),
                ('phone', models.CharField(max_length=11, verbose_name='telefone')),
                ('cell', models.CharField(blank=True, max_length=12, verbose_name='celular')),
                ('address', models.CharField(max_length=200, verbose_name='endereço')),
                ('city', models.CharField(max_length=150, verbose_name='cidade')),
                ('zip_code', models.CharField(max_length=30, verbose_name='codigo postal')),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=100, verbose_name='estado')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='cpf')),
            ],
            options={
                'verbose_name': 'cliente',
                'ordering': ['first_name', 'last_name'],
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
