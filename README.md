# ITTI

## Ambiente Virtual Python - venv (default)
virtualenv venv

## Ativação do ambiente virtual
### Linux:
source venv/bin/activate

### Windows:
venv/Script/Actvate

## Pacotes instalados
-Django

## Criação dos pacotes instalados:
pip freeze > requirements.txt

## Criação Setup Django
django-admin startproject setup .

## Execução do Projeto
1) Inicie o ambiente virtual
2) python manage.py runserver 

## Mudança Timezone e Idioma
- Go settigns.py
- LANGUAGE_CODE = 'pt-br'
- TIME_ZONE = 'America/Sao_Paulo'

## DOTENV
 1) pip install python-dotenv 
 2) Criar arquivo ".env"
 3) from dotenv import load_dotenv
 4) load_dotenv()
 5) str(os.getenv('SECRET_KEY'))

## .gitignore
1) gitignore.io
2) django
3) note arquivos ignorados no codespace ficam **cinzas**

## Criar App
1) python manage.py startapp galeria
2) add em settings.py -> INSTALLED_APPS 
3) 'galeria'
4) incluir as urls em setup -> urlpatterns
5) path("", include('galeria.urls')),

## Configuração Templates
1) settings -> itti\templates 
2) TEMPLATES ... "DIR": [os.path.join(BASE_DIR, 'templates')],