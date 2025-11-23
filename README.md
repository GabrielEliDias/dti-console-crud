# Gerenciador de livros DTI
O projeto desenvolve uma aplicação que tem como objetivo gerenciar um acervo de livros que  usando SQLite e python para rodar.

O projeto consiste em um sistema CRUD (Create, Read, Update, Delete) completo, persistindo dados em SQLite e seguindo rigorosamente os princípios de Orientação a Objetos e Arquitetura em Camadas.

## Funcionalidades
- **[C]** Create (Criar) --> Criar novos livros
- **[R]** Read (Ler) --> Ler os dados e buscar livros por ID
- **[U]** Update (Alterar) --> Edição Inteligente(pressione ENTER para manter o valor original) com tratamento híbrido de dados.
- **[D]** Delete (Remover) --> Remoção segura com confirmação visual dos dados antes da exclusão.
- **Persistência** --> Os dados são salvos automaticamente em um banco criado a partir SQLite.

## Recurso: Livro

| Propriedade       | Tipo  | Obrigatória? | Descrição                         |
| ----------------- | ----- | ------------ | --------------------------------- |
| `titulo`          | `str` | Sim          | Título do livro                   |
| `autor`           | `str` | Sim          | Nome do autor                   |
| `paginas`         | `int` | Não          | Número de páginas (inteiro)       |
| `descricao`       | `str` | Não          | Breve descrição                   |
| `data_publicacao` | `str` | Sim          | Data de publicação (`YYYY-MM-DD`) |

## Diferenciais Técnicos Implementados
1. Tratamento de Erros (Exception Handling)

    - O sistema utiliza um fluxo de propagação de exceções robusto:

    - Erros de negócio são lançados no Service (raise ValueError).

     - Erros de infraestrutura são lançados no DAO (raise sqlite3.Error).

    - Todos são capturados e tratados visualmente na View (try/except), impedindo o encerramento abrupto da aplicação (crash).

2. Tipagem e Validação Híbrida

    - Implementação de lógica para lidar com a dualidade de tipos no Update (String vinda do input vs. Objeto mantido do banco).

    - Conversão segura de tipos (str -> int, str -> date).

3. Conteinerização

    - Dockerfile: Otimizado com imagem slim e limpeza de cache.

    - Docker Compose: Configurado com volumes persistentes para garantir que os dados do SQLite não sejam perdidos ao reiniciar o container.

# Guia de Uso e Execução

Este manual descreve como configurar o ambiente, executar o Gerenciador de Livros e usar suas funcionalidades. Projetado para ser utilizado no GitHub (README.md ou docs).

---

## Execução com Docker (recomendado)

A forma mais simples de rodar a aplicação, garantindo que o ambiente seja idêntico ao de desenvolvimento.

### Pré-requisitos
- Docker e Docker Compose instalados.
- Git instalado.

### Passo a passo
1. Clone o repositório no seu computador:
```bash
git clone https://github.com/GabrielEliDias/dti-console-crud.git
```

2. Abra o terminal do projeoto e construir a imagem:
```bash
docker compose build
```

3. Rodar a aplicação (modo interativo):
```bash
docker compose run app
```

> Nota sobre persistência: o banco de dados `db_livros.db` será salvo em `src/data/` na sua máquina local. Feche e abra o container quando desejar; os livros serão mantidos.

---

## Execução local

Para rodar diretamente no sistema host.

### Pré-requisitos
- Python 3.10 ou superior.

### Passo a passo
1. Criar e ativar um ambiente virtual (opcional):
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

2. Instalar dependências:
```bash
pip install -r requirements.txt
```

3. Rodar a aplicação (a partir da raiz do projeto):
```bash
python src/main.py
```

---

## Funcionalidades

O sistema apresenta um menu numérico interativo. Principais operações:

1. Listar Livros
    - Exibe tabela formatada com todos os livros.
    - Mostra: ID, Título, Autor e um resumo curto.
    - Se a lista estiver vazia, exibe mensagem amigável.

2. Adicionar Livro
    - Formulário de cadastro.
    - Campos obrigatórios: Título e Autor.
    - Validações:
      - Data não pode ser no futuro.
      - Número de páginas deve ser positivo.
      - Formato de data: `AAAA-MM-DD`.

3. Buscar por ID
    - Exibe detalhes completos de um livro (inclui resumo completo).

4. Atualizar Cadastro
    - Edição campo a campo.
    - O sistema mostra o valor atual de cada campo.
    - Pressione ENTER para manter o valor original ou digite novo valor para alterar.

5. Remover Livro
    - Fluxo seguro: solicita o ID, exibe os dados encontrados e exige confirmação (S/N) antes de excluir.

---

## Solução de problemas comuns

- Erro: "Database is locked"
  - Causa comum: o arquivo `.db` está sendo acessado por outro programa. Feche conexões externas (por exemplo, outro cliente SQLite) ou pare outros containers que o estejam usando.

- Erro: inputs não funcionam no Docker
  - Use `docker compose run` (não `docker compose up`) para garantir que o terminal seja anexado e permita entrada de dados.

---

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

