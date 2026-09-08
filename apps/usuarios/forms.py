from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(label='Nome de Login', max_length=100, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome de login',
        }
    ))
    senha = forms.CharField(label='Senha', max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        }
    ))


class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(label='Nome de Cadastro', max_length=100, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome de cadastro',
        }
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu email',
        }
    ))

    senha_1 = forms.CharField(label='Senha', max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        }   
    ))

    senha_2 = forms.CharField(label='Senha', max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha novamente',
        }   
    ))

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome de cadastro não pode conter espaços.')
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não coincidem.')
            else:
                return senha_2