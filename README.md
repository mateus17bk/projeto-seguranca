# 🌌 Alura Space - Galeria Espacial
# Desenvolvido para Atividade de Avaliação - UNIDADES 1 e 2 - Projeto Aplicado a praticas de mercado

Uma aplicação web desenvolvida em **Python** e **Django** para gerenciamento e exibição de fotografias astronômicas, projetada sob as práticas de desenvolvimento seguro (*Secure by Design* e *Secure by Default*), contendo autenticação de usuários, busca, filtragem e **CRUD completo** (Criar, Ler, Atualizar e Deletar).

---

## 🛡️ Segurança da Aplicação & Mitigações OWASP Top 10

Em conformidade com as diretrizes do **OWASP Top 10**, o projeto implementa defesas ativas contra as principais vulnerabilidades em aplicações web:

### 1. A01:2021 / 2025 – Broken Access Control (Controle de Acesso Quebrado & IDOR)
* **Ameaça:** Acesso indevido a dados de outros usuários ou execução de operações privilegiadas sem autorização (ex.: manipulação de ID na URL para alterar/deletar fotos de terceiros via *Insecure Direct Object References - IDOR*).
* **Onde foi aplicado:** `apps/galeria/views.py` e `apps/galeria/forms.py`.
* **Como o código previne:**
  - **Guarda de Autenticação:** Todas as *views* do CRUD e busca verificam `if not request.user.is_authenticated`, redirecionando usuários não autenticados imediatamente para o login com mensagem de erro.
  - **Validação de Propriedade (Prevenção de IDOR):** Nas funções `editar_imagem` e `deletar_imagem`, o código valida explicitamente se o registro pertence ao usuário autenticado:
    ```python
    if fotografia.usuario != request.user and not request.user.is_staff:
        messages.error(request, 'Acesso negado: Você não tem permissão.')
        return redirect('index')
    ```
  - **Blindagem de Formulários:** O campo `usuario` é excluído do `FotografiaForms`, sendo injetado exclusivamente pelo servidor no momento do salvamento (`fotografia.usuario = request.user`), impossibilitando a falsificação de autoria via payload HTTP.

---

### 2. A03:2021 / 2025 – Injection (Injeção de SQL e XSS)
* **Ameaça:** Manipulação de comandos no banco de dados via parâmetros de busca/formulários (*SQL Injection*) ou injeção de scripts maliciosos nos campos de texto para execução no navegador da vítima (*Cross-Site Scripting - XSS*).
* **Onde foi aplicado:** `apps/galeria/views.py` (consultas ORM) e `templates/` (templates Django).
* **Como o código previne:**
  - **Prevenção de SQLi:** Utilização estrita do **Django ORM** com *Prepared Statements* (consultas parametrizadas) em operações como `Fotografia.objects.filter(...)` e `get_object_or_404(...)`. Não há concatenação direta de strings em comandos SQL.
  - **Prevenção de XSS:** O motor de templates do Django executa *Contextual Auto-Escaping* por padrão em todas as variáveis (`{{ fotografia.nome }}`, `{{ fotografia.descricao }}`), convertendo caracteres como `<`, `>`, `&` e `"` em entidades HTML seguras, impedindo a injeção e execução de scripts arbitrários.

---

### 3. A02 / A07:2021 / 2025 – Identification & Authentication Failures (Falhas de Autenticação e Criptografia)
* **Ameaça:** Armazenamento de credenciais em texto claro, senhas fracas suscetíveis a ataques de dicionário e interceptação/sequestro de sessões ativas.
* **Onde foi aplicado:** `apps/usuarios/views.py`, `apps/usuarios/forms.py`, `setup/settings.py` e `.env`.
* **Como o código previne:**
  - **Hash Seguro de Senhas:** As senhas dos usuários são criptografadas utilizando o algoritmo **PBKDF2 com HMAC SHA-256 e Salt dinâmico** através do método `User.objects.create_user()`, garantindo que senhas nunca sejam armazenadas em texto plano.
  - **Validação de Credenciais:** O `CadastroForm` valida o formato do nome de usuário, obrigatoriedade de campos e confirmação de senha idêntica (`clean_senha_2`).
  - **Isolamento de Segredos:** A chave criptográfica mestra (`SECRET_KEY`) é isolada em variáveis de ambiente (`.env`), com `.gitignore` estrito para evitar vazamento em repositórios públicos.
  - **Proteção de Cookies:** Flags `SESSION_COOKIE_HTTPONLY = True` e `CSRF_COOKIE_HTTPONLY = True` ativadas no `settings.py`, impedindo o roubo de sessões via scripts JavaScript.

---

### 4. A05:2021 / 2025 – Security Misconfiguration & CSRF
* **Ameaça:** Ataques de *Cross-Site Request Forgery* (CSRF), onde ações indesejadas são executadas em nome do usuário autenticado, e ataques de *Clickjacking*.
* **Onde foi aplicado:** `templates/` (todos os formulários POST) e `setup/settings.py`.
* **Como o código previne:**
  - **Tokens CSRF:** Todos os formulários `POST` contêm a tag `{% csrf_token %}` obrigatória, validada pelo middleware `django.middleware.csrf.CsrfViewMiddleware`.
  - **Anti-Clickjacking:** Configuração de cabeçalho `X_FRAME_OPTIONS = 'DENY'` para impedir o carregamento do sistema em frames/iframes maliciosos.

---

## 🚀 Funcionalidades da Aplicação

- **🔐 Autenticação Completa:**
  - Cadastro com validação de dados e hashing seguro de senhas.
  - Login e Logout com mensagens de feedback contextual.
  - Proteção de rotas em nível de middleware e controller.

- **🖼️ CRUD Completo de Fotografias:**
  - **Criar (Create):** Upload de novas imagens com título, legenda, categoria, descrição e data.
  - **Visualizar (Read):** Galeria responsiva e página com detalhes completos da imagem.
  - **Editar (Update):** Alteração de metadados e substituição da foto (restrito ao autor).
  - **Deletar (Delete):** Remoção de fotografias (restrito ao autor).

- **🔍 Busca e Filtros:**
  - Busca textual por nome de fotografia.
  - Filtros categorizados: *Nebulosa*, *Estrela*, *Galáxia* e *Planeta*.

- **💬 Alertas e Notificações:**
  - Sistema de mensagens dinâmicas de sucesso, erro e aviso (`django.contrib.messages`).

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** (v3.10+)
- **[Django](https://www.djangoproject.com/)** (v6.1)
- **[Pillow](https://python-pillow.org/)** (Processamento e upload de imagens)
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** (Gerenciamento de variáveis de ambiente)
- **[SQLite3](https://www.sqlite.org/)** (Banco de dados relacional padrão)
- **HTML5 & CSS3** (Layout responsivo personalizado)

---

## 📋 Pré-requisitos

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/downloads/) (versão 3.10 ou superior)

---

## ⚙️ Como Executar o Projeto Localmente

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

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto (onde está o arquivo `manage.py`):

- **No Windows:**
  ```powershell
  copy .env.example .env
  ```

- **No Linux / macOS:**
  ```bash
  cp .env.example .env
  ```

Abra o `.env` e defina a sua chave:
```env
SECRET_KEY=django-insecure-sua-chave-secreta-aqui
```

### 5. Executar as migrações do banco de dados
```bash
python manage.py migrate
```

### 6. (Opcional) Criar um Superusuário Administrador
```bash
python manage.py createsuperuser
```

### 7. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse no seu navegador: 👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📂 Estrutura do Projeto

```text
├── apps/
│   ├── galeria/       # Gestão de fotografias, filtros e operações CRUD
│   └── usuarios/      # Módulo de autenticação (login, cadastro, logout)
├── media/             # Armazenamento de uploads de fotos
├── setup/             # Configurações centrais do Django (settings, urls, static)
├── static/            # Arquivos estáticos coletados
├── templates/         # Templates HTML (Django Template Engine)
├── .env.example       # Modelo de variáveis de ambiente
├── .gitignore         # Regras de exclusão do controle de versão
├── manage.py          # Utilitário de linha de comando do Django
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação técnica e relatório de segurança
```

---

## 📌 Rotas da Aplicação

| Rota | Descrição | Requer Autenticação |
| :--- | :--- | :---: |
| `/` | Galeria principal de fotografias | Sim |
| `/imagem/<id>/` | Visualização detalhada de uma fotografia | Sim |
| `/nova-imagem/` | Cadastro e upload de nova fotografia | Sim |
| `/editar-imagem/<id>/` | Edição de fotografia existente | Sim (Apenas Autor) |
| `/deletar-imagem/<id>/` | Exclusão de fotografia | Sim (Apenas Autor) |
| `/buscar/` | Busca textual por nome | Sim |
| `/login/` | Autenticação de usuário | Não |
| `/cadastro/` | Registro de novos usuários | Não |
| `/logout/` | Encerramento de sessão | Sim |
| `/admin/` | Painel administrativo do Django | Sim (Staff) |

---

## 🤖 Desenvolvimento com Inteligência Artificial

Em conformidade com as diretrizes do projeto aplicado, a arquitetura, auditoria de segurança (OWASP) e documentação foram desenvolvidas e revisadas com assistência de Inteligência Artificial via IDE Antigravity / Claude Code.
