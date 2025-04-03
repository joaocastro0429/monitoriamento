from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages



def cadastro(request):
   
    if request.method=='GET':
     return render(request,'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
    
        if not senha == confirmar_senha:
         messages.add_message(request, constants.ERROR ,'senha e Confirmar senha tem que ser iguais')
         return redirect('/usuarios/cadastro')
 
        if len(senha) < 6:
            return redirect('/usuarios/cadastro')
        users = User.objects.filter(username=username)
        
        if users.exists():
            messages.add_message(request, constants.ERROR ,'usuário já existe')
            return redirect('/usuarios/cadastro')
        
    User.objects.create_user(
           
        username=username,
        password=senha
       )
       
    return redirect('/usuarios/login')  

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        if request.method == "POST":
            username= request.POST.get('username')
            senha = request.POST.get('senha')
            
            user= authenticate(request, username=username, password=senha)
            if user:
                auth.login(request,user)
                return redirect('/mentorados/')
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('login')   
                
            
    return HttpResponse(user)       
