# Sistema web para gerenciamento de lojas
## Descrição
Este projeto é uma proposta para a resolução do desafio 'Trabalho no olist' (disponível em https://github.com/olist/TechStart_2Ed)

Construído sobre uma plataforma Django com Python 3
## Instruções de instalação (configuração)

- Instale o Python 3.7.4
- Crie e acesse um ambiente virtual: `python -m venv venv`
- Clone o repositório e acesse a pasta criada
- Execute: `pip instal requirements.txt`

### Executando localmente

1. Acesse para o seu ambiente virtual: `source venv/bin/activate`
1. Instale as dependências: `pip install -r requirements.txt`
1. Crie um usuário administrador para fazer login na interface de administração do Django: `python manage.py makesuperuser`
1. Configurar banco de dados SQLite
     1. Execute migrações: `python manage.py migrate && python manage.py makemigrations`
     
1. Execute o aplicativo: `python manage.py runserver`

## Descrição do ambiente de trabalho utilizado para executar este projeto

- Mint (Ubuntu 18.04)
- IDE Pycharm
- Python 3
- Bibliotecas:
  - asgiref  |  3.3.1
  - Django   |  3.1.7
  - pip      |  21.0.1
  - pytz     |  2021.1
  - setuptools | 40.8.0
  - sqlparse  | 0.4.1