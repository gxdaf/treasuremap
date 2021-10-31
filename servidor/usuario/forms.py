from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PDevedor, PCredor, PAmplo, Cadastro


class Usuario(UserCreationForm):
    PERFIL = (
        ('', 'Escolha um tipo de perfil'),
        ('C', 'Credor'),
        ('D', 'Devedor'),
        ('A', 'Amplo')
    )
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    username = forms.CharField(max_length = 10, label='Nome de usuário')
    tp_perfil = forms.ChoiceField(choices=PERFIL, label='Tipo de Perfil')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'tp_perfil']


class PerfilC(forms.ModelForm):
    class Meta:
        model = PCredor
        fields = ['liquidez', 'aversao_ao_risco', 'ausencia_impostos', 'disponibilidade_financeira']

class PerfilD(forms.ModelForm):
    class Meta:
        model = PDevedor
        fields = ['indice']

class PerfilA(forms.ModelForm):
    class Meta:
        model = PAmplo
        fields = ['liquidez', 'aversao_ao_risco', 'ausencia_impostos', 'disponibilidade_financeira', 'indice']