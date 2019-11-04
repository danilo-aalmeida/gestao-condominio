# Generated by Django 2.2.6 on 2019-10-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('data_inicio_moradia', models.CharField(max_length=10)),
                ('data_fim_moradia', models.CharField(max_length=10)),
                ('status', models.BooleanField())
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
