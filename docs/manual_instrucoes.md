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
