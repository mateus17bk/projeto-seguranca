from django.shortcuts import render, get_object_or_404, redirect
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
   return render(request, "galeria/buscar.html", {"cards": fotografias, "termo_busca": termo_busca})

def nova_imagem(request):
    return render(request, 'galeria/nova_imagem.html')

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass