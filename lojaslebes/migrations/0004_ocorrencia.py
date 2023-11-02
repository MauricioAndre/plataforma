# Generated by Django 4.2.6 on 2023-11-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojaslebes', '0003_xmlfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ocorrencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_coleta', models.IntegerField()),
                ('tipodoc', models.CharField(max_length=10)),
                ('id_cte', models.IntegerField()),
                ('coleta_dtemissao', models.DateField()),
                ('cte_dtemissao', models.DateField()),
                ('descricao', models.CharField(max_length=255)),
                ('sequencia', models.IntegerField()),
                ('dtocorrencia', models.DateTimeField()),
                ('cnpjcpfcodigo', models.CharField(max_length=14)),
                ('razaosocial', models.CharField(max_length=255)),
                ('veiculo', models.CharField(max_length=10)),
                ('trajeto', models.IntegerField()),
                ('sequencia_trajeto', models.IntegerField()),
                ('descricao_trajeto', models.CharField(max_length=255)),
            ],
        ),
    ]
