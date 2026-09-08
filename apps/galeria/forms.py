from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada', 'usuario']
        labels = {
            'nome': 'Nome da Fotografia',
            'legenda': 'Legenda',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'foto': 'Foto',
            'data_fotografia': 'Data de registro da Fotografia',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}),
        }
