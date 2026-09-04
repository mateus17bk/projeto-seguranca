
from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

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
        
        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, 'As senhas não coincidem.')
                return redirect('cadastro') 
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de cadastro já existe.')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')


    return render(request, 'usuarios/cadastro.html',{"form": form})

