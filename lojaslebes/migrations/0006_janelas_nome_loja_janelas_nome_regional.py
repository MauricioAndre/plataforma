# Generated by Django 4.2.6 on 2023-11-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojaslebes', '0005_rename_id_cte_ocorrencia_id_ctenfse'),
    ]

    operations = [
        migrations.AddField(
            model_name='janelas',
            name='nome_loja',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='janelas',
            name='nome_regional',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
