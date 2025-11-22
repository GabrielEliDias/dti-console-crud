Poderia transformar esse documento do github "📖 Guia de Uso e Execução

Este manual contém as instruções para configurar o ambiente, executar o Gerenciador de Livros e utilizar suas funcionalidades.

## Execução com Docker (Recomendado)

A forma mais simples de rodar a aplicação, garantindo que o ambiente seja idêntico ao de desenvolvimento.

# Pré-requisitos

Docker e Docker Compose instalados.

Passo a Passo

1. Construir a imagem:
    Este comando prepara o ambiente e instala dependências.

docker compose build


2. Rodar a aplicação:
    Este comando inicia o container em modo interativo.

docker compose run app


Nota sobre Persistência: O banco de dados livraria.db será salvo automaticamente na sua pasta local src/data/. Você pode fechar o container e abrir novamente que seus livros estarão lá.

## Execução Local (Python Puro)

Caso prefira rodar diretamente no seu sistema operacional.

Pré-requisitos

Python 3.10 ou superior instalado.

Passo a Passo

Criar ambiente virtual (Opcional):

python -m venv .venv
# Ativar no Windows:
.venv\Scripts\activate
# Ativar no Linux/Mac:
source .venv/bin/activate


Instalar dependências:

pip install -r requirements.txt


Rodar o sistema:
Certifique-se de estar na raiz do projeto:

python src/main.py


## Funcionalidades do Sistema

O sistema apresenta um menu numérico interativo. Abaixo, o detalhamento de cada operação:

1. Listar Livros

Exibe uma tabela formatada com todos os livros cadastrados.

Mostra ID, Título, Autor e um resumo curto.

Se a lista estiver vazia, uma mensagem amigável é exibida.

2. Adicionar Livro

Formulário para cadastro de novos itens.

Campos Obrigatórios: Título e Autor.

Validações:

Data não pode ser no futuro.

Número de páginas deve ser positivo.

Formato de data deve ser AAAA-MM-DD.

3. Buscar por ID

Permite visualizar os detalhes completos de um livro específico (incluindo o resumo completo).

4. Atualizar Cadastro

Ferramenta de edição inteligente.

O sistema mostra o valor atual de cada campo.

Pressione ENTER para manter o valor original.

Digite algo novo para alterar apenas aquele campo.

5. Remover Livro

Fluxo seguro de exclusão.

Solicita o ID.

Mostra os dados do livro encontrado.

Exige confirmação (S/N) antes de apagar definitivamente do banco.

## Solução de Problemas Comuns

Erro: "Database is locked"

Se você estiver rodando via Docker e tentar abrir o arquivo .db com outro programa ao mesmo tempo, isso pode ocorrer. Feche as conexões externas.

Erro: Inputs não funcionam no Docker

Certifique-se de usar docker compose run e não docker compose up. O up nem sempre anexa o terminal corretamente para receber digitação." para ficar no modelo dessa escrita "# 📚 Gerenciador de Livros

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

"