from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    id_externo = models.CharField(max_length=10, null=True, blank=True)
    nome_completo = models.CharField(max_length=250)
    cnpj_cpf_codigo = models.CharField(max_length=14)