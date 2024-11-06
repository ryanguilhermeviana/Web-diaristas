# Projeto E-diaristas

### Instalando o projeto

#### Clonar o projeto
'git clone "url"'

#### Instalar dependências
'pip install -r requirements.txt'

#### Alterar as config. do banco de dados no 'settings.py'
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ediaristas',
        "USER": "root",
        "PASSWORD": "1503@2022Rg",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
'''

#### Migrar banco de dados
'python manage.py migrate'

#### Iniciar o servidor
'python manage.py runserver'