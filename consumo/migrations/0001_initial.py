# Generated by Django 2.2.6 on 2019-11-05 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartamento', '0002_auto_20191103_2315'),
        ('leitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('leitura_atual', models.DecimalField(decimal_places=2, max_digits=11)),
                ('leitura_anterior', models.DecimalField(decimal_places=2, max_digits=11)),
                ('data_leitura_atual', models.DateField()),
                ('data_leitura_anterior', models.DateField()),
                ('periodo_leitura', models.IntegerField()),
                ('consumo_atual', models.DecimalField(decimal_places=2, max_digits=11)),
                ('valor_gas', models.DecimalField(decimal_places=2, max_digits=11)),
                ('valor_pagamento', models.DecimalField(decimal_places=2, max_digits=11)),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartamento.Apartamento')),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leitor.Leitor')),
            ],
            options={
                'db_table': 'consumo',
            },
        ),
    ]