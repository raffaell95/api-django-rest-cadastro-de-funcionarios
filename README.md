# API para cadastrar e listar funcionários

## Instruções para instalação local

`python -m venv venv`

windows: `.\venv\Scripts\activate`

linux: : `source venv/bin/activate`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

## Demonstração

Deploy realizado na plataforma Heroku

repositorio git: https://github.com/raffaell95/api-django-rest-processo-seletivo.git

`https://api-igs.herokuapp.com/`

`https://api-igs.herokuapp.com/admin`


    "departments": "https://api-igs.herokuapp.com/departments/",
    "employees": "https://api-igs.herokuapp.com/employees/"


usuario de demostração:

    Login: admin
    Senha: admin123


## Autenticação

A api utiliza a lib JWT para autenticar alguns recursos
- listar, remover e atualizar departamentos
- criar, remover e atualizar funcionário

## gerando token de acesso

Deve ser passado o login e senha no body da requisição, para teste foi criado um usuario

    https://api-igs.herokuapp.com/token/
    methodo: POST
    Tipo de autenticação: Bearer token

Request:

    "username": "admin",
    "password": "admin123"

Response: 

    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjMyMDM3MiwianRpIjoiMmZmZmU1MWUzYjgxNDVjOGE3ODJiMDUzNzZjMGViMGQiLCJ1c2VyX2lkIjoxfQ.RLjkNfwYMo9w_qiHrQtOsfOXf68OkMsQ4fizFQdy7Oc",

    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjM0MjcyLCJqdGkiOiIxMzUxMWY3YWI5Yjc0NWY5OGZmNDM0YWEzZTg2NDQxZSIsInVzZXJfaWQiOjF9.U5HEeqY4jhwYWNWn847ffIOiD_RM8ljuj40ZMSSEaaA"

use https://api-igs.herokuapp.com/token/refresh para atualizar o token.


## Listando funcionários 
https://api-igs.herokuapp.com/employees/

    methodo: GET
    ordenação: ordering: -name
    filtros: search=exemplo
    Autenticação: não

Response:

    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Pedro Sousa",
            "email": "email@teste.com",
            "department": "Recursos Humanos"
        },
        {
            "name": "Rafael Ribeiro",
            "email": "testep@email.com",
            "department": "TI"
        },
        {
            "name": "Tiago Almeida",
            "email": "teste@email2.com",
            "department": "TI"
        }
    ]


use https://api-igs.herokuapp.com/employees/id para listar apenas um funcionário

## Criando funcionário

https://api-igs.herokuapp.com/employees-create

    methodo: POST
    Autenticação: sim

request:

	"name": "Rafael Ribeiro3",
	"email": "email@email.com",
	"department": 1


## Remover ou atualizar funcionário
    https://api-igs.herokuapp.com/employees-actions/id
    metodo: ['PUT', 'PATCH', 'DELETE']
    Autenticação: sim

 Para remover um colaborador basta fazer uma requisição com metodo DELETE, para https://api-igs.herokuapp.com/employees-actions/id, passando id do funcionário.

 Para atualizar um colaborador é so passar o id em: https://api-igs.herokuapp.com/employees-actions/id, com os dados a serem atualizados.

 request:

	"name": "Rafael Ribeiro update",
	"email": "email@email.com",
	"department": 1



##  Listar atualizar e remover departamento

    metodo: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    Autenticação: sim

Listando departamentos,
metodo: GET https://api-igs.herokuapp.com/departments/

listar apenas um departamento, metodo: GET https://api-igs.herokuapp.com/departments/id_departamento

Adicionando novo departamento,
metodo: POST https://api-igs.herokuapp.com/departments/

request:

    "name": "TI"


Atualiando  departamento,
metodo: PUT, PATCH https://api-igs.herokuapp.com/departments/idid_funcionario

request:

    "name": "TI"


Removendo  departamento,
metodo: DELETE https://api-igs.herokuapp.com/departments/id_funcionario





