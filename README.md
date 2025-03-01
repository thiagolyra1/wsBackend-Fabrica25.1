# Projeto para a Fábrica de Software da UNIPÊ 2025.1 -  Advice & Movie Database

Este repositório contém um projeto Django que combina duas aplicações:

1. **Movie Database** - Um sistema de gerenciamento de filmes utilizando Django Templates e PostgreSQL.
2. **Advice Database** - Uma API REST para gerenciamento de conselhos, desenvolvida com Django Rest Framework (DRF) e integrada com a API externa Advice Slip.

O projeto está containerizado com **Docker** e pode ser facilmente executado utilizando **Docker Compose**.

---

## 🎥 Vídeo do projeto rodando

https://www.youtube.com/watch?v=jS6GrdkL518

---

## 🚀 Tecnologias Utilizadas

- **Django** (Templates e DRF)
- **PostgreSQL** (Banco de dados)
- **Docker & Docker Compose** (Containerização e gerenciamento do ambiente)
- **OMDb API** (Integração para informações de filmes)
- **Advice Slip API** (Geração de conselhos aleatórios)

---

## 🎥 Movie Database

Um sistema web para gerenciamento de filmes, permitindo consulta, cadastro, edição e exclusão.

### 🔗 Funcionalidades
- 🔍 **Consulta de Filmes** - Pesquise e visualize detalhes de filmes.
- 📄 **CRUD Completo** - Cadastre, edite, liste e exclua filmes facilmente.
- 🌍 **Integração com OMDb API**

Para acessar, utilize:
```bash
http://127.0.0.1:8000/movies/
```

---

## 💬 Advice Database

Uma API criada com o Django Rest Framework que permite gerenciar uma coleção de conselhos inspiradores.

### 🔗 Funcionalidades
- 📄 **CRUD Completo** - Cadastre, edite, liste e delete conselhos.
- 💡 **Conselho Aleatório** - Receba um conselho aleatório via API.
- 🌍 **Integração com Advice Slip API**

### 📌 Endpoints
- **Obter um conselho aleatório (GET)**: [`/api_rest/advice/random_advice/`](http://127.0.0.1:8000/api_rest/advice/random_advice/)
- **Listar conselhos cadastrados (GET)**: [`/api_rest/advices/`](http://127.0.0.1:8000/api_rest/advices/)
- **Criar um novo conselho (POST)**: [`/api_rest/advice/create/`](http://127.0.0.1:8000/api_rest/advice/create/)
- **Deletar um conselho por ID (DEL)**: [`/api_rest/advice/delete/{ID}/`](http://127.0.0.1:8000/api_rest/advice/delete/{ID}/)
- **Atuzaliar um conselho por ID (PUT)**: [`/api_rest/advice/update/{ID}/`](http://127.0.0.1:8000/api_rest/advice/update/{ID}/)

Recomenda-se usar ferramentas como **Insomnia** ou **Postman** para testar os endpoints.

---

## 🛠 Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/thiagolyra1/wsBackend-Fabrica25.1.git
cd wsBackend-Fabrica25.1
```

### 2️⃣ Configurar Variáveis de Ambiente
Como é um projeto acadêmico, eu deixei um arquivo chamado ".env-example" na pasta "dotenv_files", é só renomar o arquivo para ".env" que todas as credenciais do banco PostgreSQL estarão corretas.


### 3️⃣ Construir e Iniciar os Containers
```bash
docker-compose up --build
```
Isso iniciará os containers para a aplicação Django e o banco de dados PostgreSQL.

### 4️⃣ Aplicar as Migrações do Banco de Dados
Abra um terminal dentro do container do Django:
```bash
docker exec -it nome_do_container python manage.py migrate
```

### 5️⃣ Criar um Superusuário (Opcional)
```bash
docker exec -it nome_do_container python manage.py createsuperuser
```

### 6️⃣ Acessar a Aplicação
- **Movie Database**: [`http://127.0.0.1:8000/movies/`](http://127.0.0.1:8000/movies/)
- **Advice API (DRF)**: [`http://127.0.0.1:8000/api_rest/`](http://127.0.0.1:8000/api_rest/)