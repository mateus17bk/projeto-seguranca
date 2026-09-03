from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
   fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")
   return render(request, 'galeria/index.html',{"cards": fotografias})

def imagem(request, foto_id):
   fotografia = get_object_or_404(Fotografia, pk=foto_id)
   return render(request, 'galeria/imagem.html', {"fotografia": fotografia})  

def buscar(request):
   fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")
   termo_busca = request.GET.get("q", "")
   if termo_busca:
      fotografias = fotografias.filter(nome__icontains=termo_busca)
   return render(request, "galeria/buscar.html", {"cards": fotografias, "termo_busca": termo_busca})

