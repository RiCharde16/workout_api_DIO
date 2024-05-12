# FastAPI

### Quem é o FastAPI?

Framework FastAPI, alta perfomance, Fácil de aprender, fácil de codar, pronto para produção. FastAPI é um moderno e rápido (alta perfomance) framework web para contrução de APIs com Python 3.6 ou superior, baseado nos type hits padrões do Python.

### Async

Código assincrono apenas significa que a linguagem tem um jeito de dizer para o computador / Programa que em certo ponto, ele téra que esperar algo para finalizar em outro lugar

# Projeto

### WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI. É uma API pequena, devido a ser um projeto mais hands-on simplificando nós desenvolvemos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar FastAPI.

### Modelagem de entidade e relacionamento - MER

![imagem](/workout_API.png)

## Stack da API

A API foi desenvolvida utilizando a fastapi (async). Junto dos seguintes libs: <span style="color: #FFDD68;">alembic, SQLAlchemy, pydantic</span>. Para salvar os dados sendo utilizado o postegress, por meio do docker.

## Execução da API

Para executar o projeto, criei um ambiente virtual para armazenar os pacotes e dependencias do projeto.
```
    python3 -m venv workoutapi
    workoutapi/Scripts/Acitave
```


Caso opte por usar pyenv, após instalar, execute
```
    pyenv virtualenv 3.11.4 workoutapi
    pyenv activate workoutapi
    pip install -r requirements.txt 
```

## Instalando o Invoke para automatizar tasks
Baixe o invoke no seu ambiente virtual python
``` pip
    pip install invoke
```
Usanod o invoke após a sua instalação, você pode criar um arquivo tasks.py no diretorio raiz do projeto para definir suas tarefas. para configuraro invoke para um projeto FastAPI com Uvicorn, exemplo codigo abaixo:

```python
from invoke import task
import os

@task
def run(cmd):
    # Start the Unicorn server
    cmd.run("uvicorn workout.main:app --reload")

@task
def create_migration(cmd, d):
    # Create Database migrations.
    pythonpath = os.getcwd()

    cmd.run(f"set PYTHONPATH={pythonpath} && alembic revision --autogenerate -m '{d}'")

@task
def run_migrations(cmd):
    # Run database migrations.
    pythonpath = os.getcwd()

    cmd.run(f"set PYTHONPATH={pythonpath} && alembic upgrade head")
```

Para subir o banco de dados, caso não tenha <span style="color: #508BFF">docker</span> e o <span style="color:#508BFF ">docker-compose</span> instalada, faça a instalação e logo em seguida, execute os comandos invoke do arquivo tasks.py, utilizei o comando `invoke` seguido pelo nome da tarefa:

Para criar uma migration nova, execute:
``` docker
    invoke create-migrations -d "nome_da_migration"
```

Para rodar as migrações
```
    invoke run-migrations
```

## API

Para rodar o servidor uvicorn
```
    invoke run
```
e acesse: http://127.0.0.1:8000/docs


# Referências

FastAPI https://fastapi.tiangolo.com/

Pydantic https://docs.pydantic.dev/latest/

SQLAlchemy https://docs.sqlalchemy.org/en/20/

Alembic https://alembic.sqlalchemy.org/en/latest/

docker https://www.docker.com/products/docker-desktop/

invoke https://www.pyinvoke.org/