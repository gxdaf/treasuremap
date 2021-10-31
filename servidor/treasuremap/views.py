from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from treasuremap.models import Artigos
import pickle

artigos = Artigos.objects.all()
context_art = {
    'artigos': artigos
}
def redirecionador(request, nome, context=None):
    if nome == 'treasuremap':
        return render(request, 'inicial.html', context_art)
    else:
        return render(request, f'{nome}.html')

def artigo(request, nome):
    nome = nome.split('/')[0]
    context_art['nome'] = nome

    return render(request, 'artigo.html', context_art)


def home(request):
    context = {}
    render(request, 'inicial.html', context)