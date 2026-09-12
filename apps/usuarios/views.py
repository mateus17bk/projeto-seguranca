
from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages 
import requests
import os

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome_login = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']

            usuario = authenticate(request, username=nome_login, password=senha)
            if usuario is not None:
                auth_login(request, usuario)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('index') 
            else:    
                messages.error(request, 'Nome de login ou senha inválidos.')
                return redirect('login')  
        
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        captcha_response = request.POST.get('g-recaptcha-response')
        secret_key = os.getenv("RECAPTCHA_SECRET_KEY")
        verification_url = 'https://www.google.com/recaptcha/api/siteverify'

        payload = {
            'secret': secret_key, 
            'response': captcha_response,
        }

        try:
            response = requests.post(verification_url, data=payload)
            result = response.json()
            print(f"DEBUG CAPTCHA: Resposta do Google: {result}")
            is_human = result.get('success', False)
        except Exception as e:
            print(f"DEBUG CAPTCHA: Erro na requisição: {e}")

            is_human = False
        if not is_human:
            messages.error(request, 'Por favor, confirme que você não é um robô.')
            return render(request, 'usuarios/cadastro.html', {"form": form})
    
        if form.is_valid():
            
            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha_1']

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de cadastro já existe.')
                return redirect('cadastro')

            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

