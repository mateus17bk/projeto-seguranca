from django.contrib import admin
from django import forms
from galeria.models import Fotografia


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
    list_filter = ("categoria", "publicada", "data_fotografia")
    list_per_page = 1
    form = FotografiaForm


admin.site.register(Fotografia, ListandoFotografias)