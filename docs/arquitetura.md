# Tecnologias e Arquitetura

Sistema CRUD de livraria desenvolvido para o desafio técnico da DTI Digital.

## Stack Tecnológica

- **Linguagem:** Python 3.10+
- **Banco de Dados:** SQLite (Nativo)
- **Conteinerização:** Docker & Docker Compose
- **Gerenmento de Dependências:** Pip (requirements.txt)

## Arquitetura utilizada no projeto
O sistema foi desenvolvido utilizando uma **Arquitetura em Camadas** (Layered Architecture), garantindo a separação de responsabilidades (SoC - Separation of Concerns). 
```bash
dti-console-crud/
│
├── sql/
│   └── init_db.sql        # Script que Inicia o Banco de Dados  
├── src/
│   ├── main.py            # Ponto de entrada (Orquestrador)
│   ├── models/            # Definição da Classe Livro (Entidade)
│   ├── views/             # Interface com Usuário (Inputs/Prints)
│   ├── services/          # Regras de Negócio e Validações
│   ├── repositories/      # Acesso a Dados (DAO - Data Access Object)
│   └── data/              # Arquivo do Banco de Dados (.db)
│
├── Dockerfile             # Configuração da Imagem
├── .gitignore             # Impede a Entrada de Arquivos Indevidos no Github
├── .dockerignore          # Impede a Entrada de Arquivos Indevidos no Docker
├── docker-compose.yml     # Orquestração do Container
└── requirements.txt       # Dependências
```

A aplicação segue o fluxo de responsabilidade única:

- View: Coleta dados e exibe informações. Não contém regras de negócio complexas.

- Service: O "cérebro" da aplicação. Valida regras (ex: data futura, páginas negativas), converte tipos e orquestra o fluxo.

- Repository (DAO): A única camada que conhece SQL. Responsável por transformar Objetos em linhas do banco e vice-versa (Data Mapper).

O fluxo de dados segue estritamente a direção:
```bash
View → Service → DAO → Banco
```