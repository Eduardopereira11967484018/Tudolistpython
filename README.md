# 🐍 Projeto Django + DRF + MySQL + JWT + Swagger

Este projeto é uma API desenvolvida com Django e Django REST Framework, utilizando autenticação JWT, documentação com Swagger e banco de dados MySQL.

## 📦 Requisitos

- Python 3.10+
- MySQL 5.7 ou superior
- Virtualenv (opcional, mas recomendado)

## 📁 Clonando o Projeto

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
📌 Criando o Ambiente Virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
🧪 Instalando as Dependências
bash
Copiar
Editar
pip install -r requirements.txt
Ou instale manualmente:

bash
Copiar
Editar
pip install django>=4.2
pip install djangorestframework>=3.14
pip install mysqlclient>=2.2
pip install PyJWT>=2.8
pip install drf-yasg>=1.21
⚙️ Configuração do Banco de Dados (MySQL)
Edite o arquivo settings.py com as configurações corretas:

python
Copiar
Editar
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
🔧 Migrações
bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
👤 Criar Superusuário (opcional)
bash
Copiar
Editar
python manage.py createsuperuser
🚀 Executando o Projeto
bash
Copiar
Editar
python manage.py runserver
Acesse em: http://127.0.0.1:8000

📚 Documentação Swagger
Acesse a documentação interativa em:

arduino
Copiar
Editar
http://127.0.0.1:8000/swagger/
🔐 Autenticação JWT
Utilize a rota de login para gerar o token JWT e use nos headers da API:

makefile
Copiar
Editar
Authorization: Bearer <seu_token>
Sinta-se à vontade para customizar conforme a estrutura do seu projeto. Se quiser, posso gerar também o requirements.txt automaticamente.

Copiar
Editar
