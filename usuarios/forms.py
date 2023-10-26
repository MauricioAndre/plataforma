from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    id_externo = forms.CharField(max_length=10, required=False)
    nome_completo = forms.CharField(max_length=250)
    cnpj_cpf_codigo = forms.CharField(max_length=14)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('id_externo', 'nome_completo', 'cnpj_cpf_codigo', 'email')

