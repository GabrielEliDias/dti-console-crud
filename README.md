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
