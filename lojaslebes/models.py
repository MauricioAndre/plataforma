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
    
