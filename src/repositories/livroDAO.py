import sqlite3
from datetime import datetime
from models.livro import Livro
from data.database import get_conexao

def listar_livros():
    conn = get_conexao()
    cursor = conn.cursor()

    SQL_COMANDO = 'SELECT * FROM Livros'
    
    lista_livros = []

    try:
        cursor.execute(SQL_COMANDO)
        linhas = cursor.fetchall()

        for linha in linhas:
            livro = converter_tupla_para_objeto(linha)
            lista_livros.append(livro)
            
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")
    finally:
        conn.close()
    
    return lista_livros

def adicionar_livro(livro: Livro):
    conn = get_conexao()
    cursor = conn.cursor()
    
    SQL_COMANDO = """
        INSERT INTO Livros (Titulo, Autor, DataPublicacao, Resumo, NumeroPaginas) 
        VALUES (?, ?, ?, ?, ?)
    """

    data_para_banco = livro.data_publicacao.strftime('%Y-%m-%d') if livro.data_publicacao else None

    valores = (
        livro.titulo, 
        livro.autor, 
        data_para_banco, 
        livro.resumo, 
        livro.numero_paginas
    )

    try:
        cursor.execute(SQL_COMANDO, valores)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inserir: {e}")
        raise e
    finally:
        conn.close()


def converter_tupla_para_objeto(linha):
    id_bd = linha[0]
    titulo_bd = linha[1]
    autor_bd = linha[2]
    data_str = linha[3]
    resumo_bd = linha[4]
    paginas_bd = linha[5]

    data_formatada = None
    if data_str:
        try:
            data_formatada = datetime.strptime(data_str, "%Y-%m-%d").date()
        except ValueError:
            pass 

    return Livro(
        id=id_bd,
        titulo=titulo_bd,
        autor=autor_bd,
        data_publicacao=data_formatada,
        resumo=resumo_bd,
        numero_paginas=paginas_bd
    )

def listar_livro(livro_id):
    conn = get_conexao()
    cursor = conn.cursor()

    SQL_COMANDO = 'SELECT * FROM Livros WHERE id = ?'
    
    livro_encontrado = None

    try:
        cursor.execute(SQL_COMANDO, (livro_id,))
        linha = cursor.fetchone()

        if linha:
            livro_encontrado = converter_tupla_para_objeto(linha)
            
    except sqlite3.Error as e:
        print(f"Erro ao buscar livro por ID: {e}")
    finally:
        conn.close()
    
    return livro_encontrado

def remover_livro(livro_id):
    
    conn = get_conexao()
    cursor = conn.cursor()

    SQL_COMANDO = 'DELETE FROM Livros WHERE id = ?'

    try:
        cursor.execute(SQL_COMANDO, (livro_id,))
        conn.commit()
            
    except sqlite3.Error as e:
        raise sqlite3.Error(f"Erro ao buscar livro por ID: {e}")
    finally:
        conn.close()

def alterar_livro(livro):

    conn = get_conexao()
    cursor = conn.cursor()

    SQL_COMANDO = 'UPDATE Livros SET Titulo = ?, Autor = ?, DataPublicacao = ?, Resumo = ?, NumeroPaginas = ? WHERE id = ?'

    try:
        valores = (livro.titulo, livro.autor, str(livro.data_publicacao), livro.resumo, livro.numero_paginas, livro.id)

        cursor.execute(SQL_COMANDO, valores)
        conn.commit()
            
    except sqlite3.Error as e:
        raise sqlite3.Error(f'Erro ao substituir os valores do Livro: {e}')
    finally:
        conn.close()

