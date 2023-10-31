# Generated by Django 4.2.6 on 2023-10-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='janelas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cnpjcpfcodigo', models.CharField(max_length=14)),
                ('razaosocial', models.CharField(max_length=250)),
                ('hrini_sabado', models.TimeField(blank=True, null=True)),
                ('hrfim_sabado', models.TimeField(blank=True, null=True)),
                ('hrini_seg', models.TimeField(blank=True, null=True)),
                ('hrfim_seg', models.TimeField(blank=True, null=True)),
                ('hrini_ter', models.TimeField(blank=True, null=True)),
                ('hrfim_ter', models.TimeField(blank=True, null=True)),
                ('hrini_qua', models.TimeField(blank=True, null=True)),
                ('hrfim_qua', models.TimeField(blank=True, null=True)),
                ('hrini_qui', models.TimeField(blank=True, null=True)),
                ('hrfim_qui', models.TimeField(blank=True, null=True)),
                ('hrini_sex', models.TimeField(blank=True, null=True)),
                ('hrfim_sex', models.TimeField(blank=True, null=True)),
                ('cidade', models.CharField(max_length=50)),
                ('contato_gerente', models.CharField(max_length=100)),
                ('contato_regional', models.CharField(max_length=100)),
                ('controlpoint', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]