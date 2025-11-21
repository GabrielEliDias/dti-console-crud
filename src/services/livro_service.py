from models.livro import Livro
from datetime import datetime
from repositories.livroDAO import adicionar_livro as dao_adicionar_livro
from repositories.livroDAO import listar_livro as dao_listar_livro_por_id
from repositories.livroDAO import remover_livro as dao_remover_livro_por_id

def adicionar_livro(titulo, autor, data_publicacao, resumo, numero_paginas):

    if not titulo:
        raise ValueError("O título do livro não pode ser vazio.")

    if not autor:
        raise ValueError("O autor do livro não pode ser vazio.")
    
    try:
        data_publicacao_dt = datetime.strptime(data_publicacao, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("A data de publicação deve estar no formato AAAA-MM-DD.")
    
    numero_paginas_int = None
    if numero_paginas:
        try:
            numero_paginas_int = int(numero_paginas)
            if numero_paginas_int <= 0:
                raise ValueError("O número de páginas deve ser um inteiro positivo.")
        except ValueError:
            raise ValueError("O número de páginas deve ser um inteiro válido.")

    
    livro = Livro(
        id=None,
        titulo=titulo,
        autor=autor,
        data_publicacao=data_publicacao_dt, 
        resumo=resumo,
        numero_paginas=numero_paginas_int 
    )

    dao_adicionar_livro(livro)

def livro_por_id(livro_id):
    
    if not livro_id:
        raise ValueError("O ID do livro não pode ser vazio.")
    
    try:
        livro_id_int = int(livro_id)
        if livro_id_int <= 0:
            raise ValueError("O ID do livro deve ser um inteiro positivo.")
    except ValueError:
        raise ValueError("O ID do livro deve ser um inteiro válido.")
    
    livro = dao_listar_livro_por_id(livro_id_int)

    if not livro:
        raise ValueError(f"Nenhum livro encontrado com o ID {livro_id_int}.")
    
    return livro

def remover_livro_por_id(livro_id):
    if not livro_id:
        raise ValueError("O ID do livro não pode ser vazio.")
    
    try:
        livro_id_int = int(livro_id)
        if livro_id_int <= 0:
            raise ValueError("O ID do livro deve ser um inteiro positivo.")
    except ValueError:
        raise ValueError("O ID do livro deve ser um inteiro válido.")
    
    livro = dao_listar_livro_por_id(livro_id_int)

    if not livro:
        raise ValueError(f"Nenhum livro encontrado com o ID {livro_id_int}.")
    
    dao_remover_livro_por_id(livro_id_int)
