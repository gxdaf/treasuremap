from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PAmplo, PCredor, PDevedor, Cadastro
from .forms import Perg

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Cadastro.objects.create(usuario=instance, tp_perfil=request.POST['tp_perfil'])


@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, **kwargs):
    instance.profile.save()