from django.shortcuts import render, redirect
from .models import Mentorados, Navigators
from django.contrib.messages import constants
from django.contrib import messages



def mentorados(request):
    if request.method == 'GET':
        navigators = Navigators.objects.filter(user=request.user)
        mentorados = Mentorados.objects.filter(user=request.user)
        
        estagios_flat = [i[1] for i in Mentorados.estagio_choices]
        qtd_estagios = []

        for i, j in Mentorados.estagio_choices:
            qtd_estagios.append(Mentorados.objects.filter(estagio=i).count())

    
        return render(request, 'mentorados.html', {'estagios': Mentorados.estagio_choices, 'navigators': navigators, 'mentorados': mentorados, 'estagios_flat': estagios_flat, 'qtd_estagios': qtd_estagios})
    else:
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        estagio = request.POST.get('estagio')
        navigator = request.POST.get('navigator')
        
        # Renomeie a variável para evitar conflito com o nome da função
        mentorados = Mentorados(
            nome=nome,
            foto=foto,
            estagio=estagio,
            navigator_id=navigator,
            user=request.user
        )
        mentorados.save()
        
        messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso.')
        return redirect('mentorados')