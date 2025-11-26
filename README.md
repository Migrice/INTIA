# Analyse:

https://docs.google.com/document/d/1SVsSLlh-AiIN3j8VokIaJQTZ0G8GTy0oTiPTKIrw4vw/edit?usp=sharing

## Prerequisites

Before to get started these are the tools that you need.

[x] Python 3.12+ (Complete with a [link](https://www.python.org/) related to the installation)

[x] Poetry 2.1+ (Complete with a [link](https://python-poetry.org/) related to the installation)

[x] VS Code (Complete with a [link](https://code.visualstudio.com/) related to the installation)

## Installation and configuration

Clone the project

Move to workdir

```sh
cd intia
```

Refer to **.env.example** file to create your own **.env** file to configurate Auth App

> **_ATTENTION_** The app need specifics variables environments to launch, refer to .env.example file

<br />

#### I.1.1. Base installation

Install python dependencies

```sh
poetry install --all-extras
```

Active virtual environment

```sh
poetry shell
```

---

```sh
python manage.py migrate
```

Run App

```sh
python manage.py runserver
```

## Deploiement

Le frontend sera deployé sur un serveur à part de meme que le backend. En premier temps, on va dockeriser les deux applications. On va ensuite les conteunariser à l'aide d'un docker compose. Puis on va utiliser Jenkins pour automatiser le deploiment

On peut deployer par exemple sur un serveur Hostinger
