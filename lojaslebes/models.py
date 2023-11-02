from django.db import models


class janelas(models.Model):
    id = models.AutoField(primary_key=True)
    cnpjcpfcodigo = models.CharField(max_length=14)
    razaosocial = models.CharField(max_length=250)
    hrini_sabado = models.TimeField(null=True, blank=True)
    hrfim_sabado = models.TimeField(null=True, blank=True)
    hrini_seg = models.TimeField(null=True, blank=True)
    hrfim_seg = models.TimeField(null=True, blank=True)
    hrini_ter = models.TimeField(null=True, blank=True)
    hrfim_ter = models.TimeField(null=True, blank=True)
    hrini_qua = models.TimeField(null=True, blank=True)
    hrfim_qua = models.TimeField(null=True, blank=True)
    hrini_qui = models.TimeField(null=True, blank=True)
    hrfim_qui = models.TimeField(null=True, blank=True)
    hrini_sex = models.TimeField(null=True, blank=True)
    hrfim_sex = models.TimeField(null=True, blank=True)
    cidade = models.CharField(max_length=50)
    contato_gerente = models.CharField(max_length=100)
    contato_regional = models.CharField(max_length=100)
    
class xmlfile(models.Model):
    file = models.FileField(upload_to='xml_files/',blank=True,null=True)


class ocorrencia(models.Model):
    id = models.AutoField(primary_key=True)
    id_coleta = models.IntegerField()
    tipodoc = models.CharField(max_length=10)
    id_ctenfse = models.IntegerField()
    coleta_dtemissao = models.DateField()
    cte_dtemissao = models.DateField()
    descricao = models.CharField(max_length=255)
    sequencia = models.IntegerField()
    dtocorrencia = models.DateTimeField()
    cnpjcpfcodigo = models.CharField(max_length=14)
    razaosocial = models.CharField(max_length=255)
    veiculo = models.CharField(max_length=10)
    trajeto = models.IntegerField()
    sequencia_trajeto = models.IntegerField()
    descricao_trajeto = models.CharField(max_length=255)