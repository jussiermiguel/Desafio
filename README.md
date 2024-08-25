# Projeto Django CRUD

## Descrição

Este projeto é uma aplicação Django que implementa um CRUD completo para duas entidades (`Academia` e `Consulta`). Além disso, o projeto utiliza um banco de dados PostgreSQL e inclui uma interface web básica para visualização dos dados.

## Requisitos

- Python 3.11 ou superior
- PostgreSQL
- pip (gerenciador de pacotes Python)

## Instalação

### 1. Clone o Repositório
### 2. Crie e Ative um Ambiente Virtual(python -m venv venv) (venv/Script/activate)
### 3. Instale as dependências no arquivo requirements.txt (pip install -r requirements.txt)
### 4. Realize as migrações(makemigrations e migrate)
### 5. Execute o servidor (python manage.py runserver)

## No navegador digite e entre no site "http://127.0.0.1:8000/"

## Na lógica que eu usei, uma consulta só pode ser feita por alunos da academia. Ou seja, não é possível adicionar uma consulta a uma pessoa que não conste no banco de dados da academia.

## Depois de cadastrar o aluno na academia, ele pode ir ser cadastrado na consulta de um nutricionista. Com alguns dados coletados nessa consulta, o IMC da pessoa é calculado automaticamente e aparecerá na lista de consultas.
