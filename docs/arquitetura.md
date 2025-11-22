# Gerenciador de Livros

Sistema CRUD de livraria desenvolvido para o desafio técnico da DTI Digital.

## Stack Tecnológica

- **Linguagem:** Python 3.10+
- **Banco de Dados:** SQLite (Nativo)
- **Conteinerização:** Docker & Docker Compose
- **Gerenmento de Dependências:** Pip (requirements.txt)

## Padrão de Arquitetura

O sistema foi desenvolvido utilizando uma **Arquitetura em Camadas** (Layered Architecture), garantindo a separação de responsabilidades (SoC - Separation of Concerns). O fluxo de dados segue estritamente a direção:

**View → Service → DAO → Banco**

### Diagrama de Responsabilidades

- **View (Camada de Apresentação):**
  - Responsável APENAS pela interação com o usuário (I/O)
  - Coleta inputs e exibe mensagens
  - Não executa regras de negócio complexas
  - Não acessa o banco de dados diretamente

- **Service (Camada de Negócio):**
  - O "cérebro" da aplicação
  - Orquestra o fluxo de dados
  - Realiza validações de negócio (ex: impedir datas futuras, validar números de páginas)
  - Converte tipos de dados (ex: String da View para Objeto Date do Model)

- **Repository / DAO (Camada de Persistência):**
  - Única camada que conhece SQL
  - Implementa o padrão Data Mapper: converte tuplas do banco em objetos Python (Model) e vice-versa
  - Protegido contra SQL Injection através do uso de parameters binding (?)

## Estrutura de Pastas

A organização do código reflete a arquitetura escolhida:
src/
├── main.py                 # Entrypoint: Apenas inicia o Menu Principal
├── models/                 # Entidades (POJO/POCO)
│   └── livro.py           # Classe Livro (atributos e encapsulamento)
├── views/                 # Telas do Console
│   └── livro_view.py      # Menus, Inputs e Prints formatados
├── services/              # Lógica de Negócio
│   └── livro_service.py   # Validações e chamadas ao DAO
├── repositories/          # Acesso a Dados
│   └── livroDAO.py        # SQL (INSERT, UPDATE, DELETE, SELECT)
└── data/                  # Persistência
    ├── database.py        # Configuração de conexão SQLite
    └── livraria.db        # Arquivo do banco (gerado automaticamente)


## Diferenciais Técnicos Implementados

### 1. Tratamento de Erros (Exception Handling)

O sistema utiliza um fluxo de propagação de exceções robusto:
- Erros de negócio são lançados no Service (`raise ValueError`)
- Erros de infraestrutura são lançados no DAO (`raise sqlite3.Error`)
- Todos são capturados e tratados visualmente na View (`try/except`), impedindo o encerramento abrupto da aplicação (crash)

### 2. Tipagem e Validação Híbrida

- Implementação de lógica para lidar com a dualidade de tipos no Update (String vinda do input vs. Objeto mantido do banco)
- Conversão segura de tipos (`str -> int`, `str -> date`)

### 3. Conteinerização

- **Dockerfile:** Otimizado com imagem slim e limpeza de cache
- **Docker Compose:** Configurado com volumes persistentes para garantir que os dados do SQLite não sejam perdidos ao reiniciar o container
