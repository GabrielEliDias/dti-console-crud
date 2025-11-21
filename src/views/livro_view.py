import textwrap
from repositories.livroDAO import listar_livros
from services.livro_service import adicionar_livro, livro_por_id, remover_livro_por_id

def dados_livro_view():
    print('\n')
    print('--------- Buscar livro por ID ---------')
    print('\n')

    try:
        livro_id = int(input('Informe o ID do livro que deseja buscar: '))
    except ValueError:
        print("ID inválido. Tente novamente.")
        return
    
    livro = livro_por_id(livro_id)

    print('\n ')

    print('--- Detalhes do livro solicitado ---')
    print(f"[ID: {livro.id}] {livro.titulo} - {livro.autor}")
        
    print(f"      {livro.numero_paginas} págs | Lançamento: {livro.data_publicacao}")
    print(f'Resumo:')

    if not livro.resumo == None:
        print(textwrap.fill(livro.resumo, width=60))
    else:
        print(f'Não foi cadastrado um resumo para o {livro.titulo}')
        
    print("-" * 40)
        
    print('\n')



def listar_livros_view():

    print("\n")  
    print('---------- Lista de Livros ----------')
    print("\n")  

    livros = listar_livros()

    for livro in livros:
        print(f"[ID: {livro.id}] {livro.titulo} - {livro.autor}")
        
        print(f"      {livro.numero_paginas} págs | Lançamento: {livro.data_publicacao}")
        print(f'Resumo:')

        if not livro.resumo == None:
            print(textwrap.fill(livro.resumo, width=60))
        else:
            print(f'Não foi cadastrado um resumo para o {livro.titulo}')
        
        print("-" * 40)
        
        print('\n')

def registrar_livro_view():
    print("\n")
    print('--------- Registrar novo livro ---------')

    titulo = input('Título do livro: ')
    autor = input('Autor do livro: ')
    data_publicacao = input('Data de publicação (AAAA-MM-DD): ')
    resumo = input('Resumo do livro: ')
    numero_paginas = input('Número de páginas: ')

    print("\n" + "-"*40)
    print("CONFIRA OS DADOS:")
    print(f"Título:   {titulo}")    
    print(f"Autor:    {autor}")
    print(f"Data:     {data_publicacao}")
    print(f"Páginas:  {numero_paginas}")
        
    resumo_display = textwrap.shorten(resumo, width=50) if resumo else "---"
    print(f"Resumo:   {resumo_display}")
    print("-" * 40)

    confirmar = input('Confirmar cadastro? (S/N): ').strip().upper()
    if confirmar == 'S':
        try:
            adicionar_livro(titulo, autor, data_publicacao, resumo, numero_paginas)
            print("Livro gravado com sucesso.")
        except ValueError as erro_que_veio_do_service:
            print(f"{erro_que_veio_do_service}")
            print("Tente novamente.")
        except Exception as erro_critico:
            print(f'{erro_critico}')
            print("Após verificar o erro, tente novamente mais tarde.")
    else: 
        print("Cadastro cancelado pelo usuário.")

def deletar_livro_view():

    print('\n')
    print('---------- Remover livro por id ----------')
    print('\n')

    try:
        livro_id = int(input('Informe o ID do livro que deseja buscar: ').strip())
    except ValueError as e:
        print(f"ID inválido {e}. Tente novamente.")
        return
    
    livro = livro_por_id(livro_id)

    print('\n ')

    if not livro:
        print(f"Livro com ID {livro_id} não encontrado.")
        return

    print('--- Deseja remover o livro detalhado a baixo? ---')
    print(f"[ID: {livro.id}] {livro.titulo} - {livro.autor}")
        
    print(f"      {livro.numero_paginas} págs | Lançamento: {livro.data_publicacao}")
    print(f'Resumo:')

    if not livro.resumo == None:
        print(textwrap.fill(livro.resumo, width=60))
    else:
        print(f'Não foi cadastrado um resumo para o {livro.titulo}')
        
    print("-" * 40)
        
    print('\n')

    if input('Confirme a remoção do livro (S \ N) ').strip().upper() == 'S':
        remover_livro_por_id(livro_id)

        print('Remoção do livro confirmado com sucesso.')
    else:
        print('Cancelando a remoção do livro escolhido.....') 

def alterar_livro_info_view():
    print('\n')
    print('---------- Alterar informações de livro por id ----------')
    print('\n')

    # Pedir o id do livro

    # buscar o id e perguntar para confirmar se esse é o livro que quer mudar(view)

    # buscar(DAO) e criar uma cópia do objeto para modificar(service)

    # Salvar a nova cópia e enviar ao Service para enviar ao DAO e salver no final

    # Iremos realizar uma lógica parecia com a de criação de um livro, onde vamos perguntar no que a pessoa quer mudar cada coisa. Se a pessoa der "" devemos não modificar os dados originais.

    # Salvar a informação no mesmo ponto de id do banco de dados
