from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    if request.method=='GET':
     return render(request,'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
    return HttpResponse(f'Username: {username}, Senha: {senha}, Confirmar Senha: {confirmar_senha}')
    
