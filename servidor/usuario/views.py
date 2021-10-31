from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from treasuremap.views import redirecionador
from .forms import Usuario, PerfilA, PerfilC, PerfilD
from .models import Cadastro
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PDevedor, PCredor, PAmplo

@csrf_exempt
def registrar(request):
    if request.method == 'POST':
        form = Usuario(request.POST)
        if form.is_valid():
            form.save()
            user_id = int(request.user.id)
            user = User.objects.get(id=user_id)
            tp_perfil = form.cleaned_data['tp_perfil']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            cad = Cadastro(usuario=user, tp_perfil = tp_perfil)
            cad.save()
            return redirect('cadperfil')
    else: 
        form = Usuario()
        context = {
            'form': form
        }
        return render(request, 'cadastro.html', context)

def dadosperfil(request):
    user_id = int(request.user.id)
    tp_perfil = Cadastro.objects.get(usuario_id = user_id)
    tp_perfil = tp_perfil.tp_perfil
    if request.method == 'POST':
        if tp_perfil == 'A':
            liquidez = request.POST['liquidez']
            aversao_ao_risco = request.POST['aversao_ao_risco']
            ausencia_impostos = request.POST['ausencia_impostos']
            disponibilidade_financeira = request.POST['disponibilidade_financeira']
            indice = request.POST['indice']
            usuario_id = int(request.user.id)
            form = PerfilA(request.POST)
            if form.is_valid():
                p = PAmplo(liquidez = liquidez, aversao_ao_risco = aversao_ao_risco, ausencia_impostos = ausencia_impostos, disponibilidade_financeira = disponibilidade_financeira, indice = indice, usuario_id = usuario_id)
                p.save()
                messages.success(request, f'Perfil criado com sucesso, {request.user.first_name}')
                return redirect('treasuremap')
        elif tp_perfil == 'C':
            liquidez = request.POST['liquidez']
            aversao_ao_risco = request.POST['aversao_ao_risco']
            ausencia_impostos = request.POST['ausencia_impostos']
            disponibilidade_financeira = request.POST['disponibilidade_financeira']
            usuario_id = int(request.user.id)
            form = PerfilC(request.POST)
            if form.is_valid():
                p = PCredor(liquidez = liquidez, aversao_ao_risco = aversao_ao_risco, ausencia_impostos = ausencia_impostos, disponibilidade_financeira = disponibilidade_financeira, usuario_id = usuario_id)
                p.save()
                messages.success(request, f'Perfil criado com sucesso, {request.user.first_name}')
                return redirect('treasuremap')
        elif tp_perfil == 'D':
            indice = request.POST['indice']
            usuario_id = int(request.user.id)
            form = PerfilD(request.POST)
            if form.is_valid():
                p = PDevedor(indice = indice, usuario_id = usuario_id)
                p.save()
                messages.success(request, f'Perfil criado com sucesso, {request.user.first_name}')
                return redirect('treasuremap')
    else:
        if tp_perfil == 'A':
            form = PerfilA()
            context = {
                'form': form
            }
            return render(request, 'cadperfil.html', context)
        elif tp_perfil == 'D':
            form = PerfilD()
            context = {
                'form': form
            }
            return render(request, 'cadperfil.html', context)
        elif tp_perfil == 'C':
            form = PerfilC()
            context = {
                'form': form
            }
            return render(request, 'cadperfil.html', context)

@login_required
def perfil(request):
    return render(request, 'perfil.html')