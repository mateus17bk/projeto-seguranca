# 🌌 Alura Space - Galeria Espacial
# Desenvolvido para Atividade de Avaliação - UNIDADES 1 e 2 - Projeto Aplicado a praticas de mercado

Uma aplicação web desenvolvida em **Python** e **Django** para gerenciamento e exibição de fotografias do espaço, contando com sistema completo de autenticação de usuários, busca, filtragem e operações de **CRUD** (Criar, Ler, Atualizar e Deletar).

---

## 🚀 Funcionalidades

- **🔐 Autenticação de Usuários:**
  - Cadastro de novos usuários com validação de dados e senhas.
  - Login e Logout com mensagens de feedback.
  - Controle de acesso e proteção de rotas (apenas usuários autenticados gerenciam e visualizam a galeria).

- **🖼️ CRUD de Fotografias:**
  - **Criar (Create):** Upload de novas imagens espaciais com título, legenda, categoria, descrição e data.
  - **Visualizar (Read):** Visualização de cards na página inicial e página com detalhes completos da imagem.
  - **Editar (Update):** Formulário para alteração de informações e substituição de foto.
  - **Deletar (Delete):** Remoção de fotografias cadastradas.

- **🔍 Busca e Filtros:**
  - Campo de busca por nome da fotografia.
  - Filtros rápidos por categorias: *Nebulosa*, *Estrela*, *Galáxia* e *Planeta*.

- **💬 Mensagens e Notificações:**
  - Alertas interativos de sucesso, erro e atenção utilizando o sistema `django.contrib.messages`.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** (v3.10+)
- **[Django](https://www.djangoproject.com/)** (v6.1)
- **[Pillow](https://python-pillow.org/)** (Processamento e upload de imagens)
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** (Gerenciamento de variáveis de ambiente)
- **[SQLite3](https://www.sqlite.org/)** (Banco de dados padrão)
- **HTML5 & CSS3** (Layout responsivo personalizado)

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:
- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/downloads/) (recomendado versão 3.10 ou superior)

---

## ⚙️ Como Executar o Projeto Localmente

Siga o passo a passo abaixo para rodar o projeto em sua máquina:

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
```

### 2. Criar e ativar o ambiente virtual (venv)

- **No Windows (Prompt de Comando ou PowerShell):**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **No Linux ou macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

> *Dica:* Quando o ambiente virtual estiver ativo, você verá `(venv)` no início da linha de comando do terminal.

### 3. Instalar as dependências
Com o ambiente virtual ativado, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto (onde está o arquivo `manage.py`):

- **No Windows (PowerShell):**
  ```powershell
  copy .env.example .env
  ```

- **No Linux / macOS / Bash:**
  ```bash
  cp .env.example .env
  ```

Abra o arquivo `.env` criado e defina a sua `SECRET_KEY` (pode ser qualquer texto longo ou uma chave gerada pelo Django):
```env
SECRET_KEY=django-insecure-sua-chave-secreta-aqui
```

### 5. Executar as migrações do banco de dados
Crie a estrutura das tabelas no banco de dados SQLite:
```bash
python manage.py migrate
```

### 6. (Opcional) Criar um Superusuário (Admin)
Caso queira acessar o painel administrativo do Django (`/admin`):
```bash
python manage.py createsuperuser
```
Informe nome de usuário, e-mail e senha conforme solicitado no terminal.

### 7. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Agora acesse no seu navegador:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📂 Estrutura de Pastas

```text
├── apps/
│   ├── galeria/       # App responsável pelas fotografias, filtros e CRUD
│   └── usuarios/      # App responsável pela autenticação (login, cadastro, logout)
├── media/             # Armazenamento de uploads de fotos feitos pelos usuários
├── setup/             # Configurações globais do Django (settings, urls, static)
├── static/            # Arquivos estáticos coletados
├── templates/         # Arquivos de templates HTML (Django Templates)
├── .env.example       # Exemplo de arquivo de variáveis de ambiente
├── .gitignore         # Arquivos ignorados pelo Git
├── manage.py          # Utilitário de linha de comando do Django
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

---

## 📌 Rotas Principais da Aplicação

| Rota | Descrição |
| :--- | :--- |
| `/` | Página inicial com a galeria de imagens |
| `/imagem/<id>/` | Página de detalhes de uma fotografia |
| `/nova-imagem/` | Formulário para adicionar uma nova imagem |
| `/editar-imagem/<id>/` | Formulário para editar uma fotografia existente |
| `/deletar-imagem/<id>/` | Ação para remover uma fotografia |
| `/buscar/` | Busca de fotografias por nome |
| `/login/` | Página de autenticação de usuário |
| `/cadastro/` | Página de registro de novo usuário |
| `/logout/` | Encerra a sessão do usuário conectado |
| `/admin/` | Painel administrativo do Django |

---

## 💡 Dicas de Uso

1. **Primeiro Acesso:** Crie uma conta na tela de [Cadastro](/cadastro/) ou use a conta de superusuário.
2. **Adicionar Imagens:** Após logar, clique em **"Nova imagem"** no menu lateral para cadastrar suas fotos espaciais.
3. **Gerenciar:** Ao clicar em uma imagem na galeria, utilize os botões **"Editar Imagem"** e **"Deletar Imagem"** para atualizá-la ou excluí-la.

---

Feito com 💜 por você! Sinta-se à vontade para contribuir com melhorias.
