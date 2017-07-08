# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 04:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400)),
                ('type', models.CharField(blank=True, choices=[('ast', 'asset'), ('lib', 'liability'), ('oe', 'owners equity'), ('exp', 'expense'), ('inc', 'income')], max_length=5)),
                ('head_code', models.IntegerField(blank=True, null=True)),
                ('ledger_head_code', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounting.AccountHead')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accounting_account_head',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('voucher_type', models.SmallIntegerField(choices=[(1, 'Purchase'), (5, 'Expense'), (3, 'Journal'), (4, 'Contra'), (5, 'Payment'), (6, 'Receipt'), (7, 'Debit note'), (8, 'Credit note')])),
                ('voucher_number', models.CharField(blank=True, max_length=255)),
                ('voucher_status', models.SmallIntegerField(choices=[(0, 'disabled'), (1, 'entered'), (2, 'processing'), (3, 'processed')])),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounting.Transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('dr', 'debit'), ('cr', 'credit')], max_length=5)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=18)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_head', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.AccountHead')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.Transaction')),
            ],
            options={
                'db_table': 'accounting_transaction_details',
            },
        ),
    ]
