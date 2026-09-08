from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.forms import FotografiaForms
from apps.galeria.models import Fotografia
from django.contrib import messages 

def index(request):
   if not request.user.is_authenticated:
      messages.error(request, 'Você precisa estar logado para acessar a galeria.')
      return redirect('login')
   
   fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")
   return render(request, 'galeria/index.html',{"cards": fotografias})

def imagem(request, foto_id):
   fotografia = get_object_or_404(Fotografia, pk=foto_id)
   return render(request, 'galeria/imagem.html', {"fotografia": fotografia})  

def buscar(request):
   if not request.user.is_authenticated:
      messages.error(request, 'Você precisa estar logado para acessar a galeria.')
      return redirect('login')
   fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")
   termo_busca = request.GET.get("buscar") or request.GET.get("q", "")
   if termo_busca:
      fotografias = fotografias.filter(nome__icontains=termo_busca)
   return render(request, "galeria/index.html", {"cards": fotografias, "termo_busca": termo_busca})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria.')
        return redirect('login')

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            fotografia = form.save(commit=False)
            fotografia.usuario = request.user
            fotografia.save()
            messages.success(request, 'Fotografia adicionada com sucesso!')
            return redirect('index')
    else:
        form = FotografiaForms()
    return render(request, 'galeria/nova_imagem.html', {"form": form})

def editar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria.')
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {"form": form, 'foto_id': foto_id})


def deletar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria.')
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia deletada com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria.')
        return redirect('login')

    fotografias = Fotografia.objects.filter(publicada=True, categoria=categoria).order_by("-data_fotografia")
    return render(request, "galeria/index.html", {"cards": fotografias, "categoria": categoria})