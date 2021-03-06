# Generated by Django 2.0.4 on 2018-05-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('logon', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('senha', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('dtexpiracao', models.DateField(blank=True, db_column='dtExpiracao', null=True)),
                ('idadministrador', models.AutoField(db_column='idAdministrador', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
    ]
