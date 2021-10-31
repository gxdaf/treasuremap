from django.db import models
from django import forms
from django.contrib.auth.models import User

class Cadastro(models.Model):
    usuario = models.OneToOneField(User, primary_key = True,  on_delete=models.CASCADE)
    tp_perfil = models.CharField(max_length=2, default='A')
    class Meta:
        db_table = 'tp_perfil'

class PDevedor(models.Model):
    usuario = models.OneToOneField(User,primary_key = True,  on_delete=models.CASCADE)
    indice = models.CharField(choices=[('IPCA', 'IPCA'), ('IGPM', 'IGP-M'), ('PIB', 'PIB'), ('SELIC', 'Selic')], default='SELIC', max_length=15)
    class Meta:
        db_table = 'perfil_d'

class PCredor(models.Model):
    usuario = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    liquidez = models.CharField(choices=[('S', 'Seca'), ('I', 'Imediata'), ('G', 'Geral'), ('C', 'Corrente'), ('PNO', 'Prefiro não optar')], default='C', max_length=15)
    aversao_ao_risco = models.CharField(choices=[('A', 'Alta'), ('M', 'Moderada'), ('B', 'Baixa'), ('I', 'Inexistente')], default='I', max_length=15)
    ausencia_impostos = models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=15)
    disponibilidade_financeira = models.FloatField(default=30)
    class Meta:
        db_table = 'perfil_c'

class PAmplo(models.Model):
    usuario = models.OneToOneField(User,primary_key = True,  on_delete=models.CASCADE)
    indice = models.CharField(choices=[('IPCA', 'IPCA'), ('IGPM', 'IGP-M'), ('PIB', 'PIB'), ('SELIC', 'Selic')], default='SELIC', max_length=15)
    liquidez = models.CharField(choices=[('S', 'Seca'), ('I', 'Imediata'), ('G', 'Geral'), ('C', 'Corrente'), ('PNO', 'Prefiro não optar')], default='C', max_length=15)
    aversao_ao_risco = models.CharField(choices=[('A', 'Alta'), ('M', 'Moderada'), ('B', 'Baixa'), ('I', 'Inexistente')], default='I', max_length=15)
    ausencia_impostos = models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=15)
    disponibilidade_financeira = models.FloatField(default=30)
    
    def __str__(self):
        return f'Perfil de {self.user.username}'

    class Meta:
        db_table = 'perfil_a'