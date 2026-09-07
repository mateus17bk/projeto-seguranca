from django.contrib import admin
from django import forms
from apps.galeria.models import Fotografia


class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        fields = '__all__'
        widgets = {
            'foto': forms.ClearableFileInput(),
        }


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada", "data_fotografia")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria", "publicada", "data_fotografia", "usuario")
    list_per_page = 10
    form = FotografiaForm


admin.site.register(Fotografia, ListandoFotografias)