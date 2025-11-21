import textwrap
from data.database import inicializar_banco
from repositories.livroDAO import listar_livros
from services.livro_service import adicionar_livro, livro_por_id, remover_livro_por_id, modificar_livro_por_id

def main_menu():

    inicializar_banco()

    print('----------------------------------------')
    print('  Bem-vindo a gerenciador de livros!')
    print('----------------------------------------')
    while True:
        print('\n')

        print('-- Qual ação deseja realizar no gerenciador de livros? --')
        print('1 - Listar todos os livros do gerenciador de livros')
        print('2 - Adicionar livro ao gerenciador de livros')
        print('3 - Buscar livro por ID')
        print('4 - Atualizar o cadastro de um livro')
        print('5 - Remover livro do gerenciador de livros')
        print('6 - Sair do programa')
        print('\n')

        escolha = input('>')

        if escolha == '1':
            listar_livros_view()
        elif escolha == '2':
            registrar_livro_view()
        elif escolha == '3':
            dados_livro_view()
        elif escolha == '4':
            alterar_livro_info_view()
        elif escolha == '5':
            deletar_livro_view()
        elif escolha == '6':
            print('Fechando o programa.....')
            return
        else: 
            print("Comando não identificado, por favor insira o comando novamente.")
            continue


def livro_detalhes_view(livro):

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

def dados_livro_view():
    print('\n')
    print('--------- Buscar livro por ID ---------')
    print('\n')

    livro_id = input('Informe o ID do livro que deseja buscar: ')

    if not livro_id.isdigit():
        print('Erro: Não foi digitado numero algum')
        return

    try:
        livro_id_int = int(livro_id)
    except ValueError:
        print("ID inválido. Tente novamente.")
        return
    
    try:
        livro = livro_por_id(livro_id_int)
    except ValueError as e:
        print(f'Erro: {e}')
        return
    
    if livro == None:
        print('O id digitado não existe!')
        return

    livro_detalhes_view(livro)



def listar_livros_view():

    print("\n")  
    print('---------- Lista de Livros ----------')
    print("\n")  

    livros = listar_livros()

    for livro in livros:
        livro_detalhes_view(livro)

def registrar_livro_view():
    print("\n")
    print('--------- Registrar novo livro ---------')
    print('Todos que forem obrigatório devem ser preenchidos.')

    titulo = input('Título do livro(Obrigatório): ')
    autor = input('Autor do livro(Obrigatório): ')
    data_publicacao = input('Data de publicação (AAAA-MM-DD)(Obrigatório): ')
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
    
    try:
        livro = livro_por_id(livro_id)
    except ValueError as e:
        print(f'Erro: {e}')
        return
    
    if livro == None:
        print('O id digitado não existe!')
        return
    
    print('\n ')

    if not livro:
        print(f"Livro com ID {livro_id} não encontrado.")
        return

    print('--- Deseja remover o livro detalhado a baixo? ---')
    
    livro_detalhes_view(livro)

    if input('Confirme a remoção do livro (S \ N) ').strip().upper() == 'S':
        remover_livro_por_id(livro_id)

        print('Remoção do livro confirmado com sucesso.')
    else:
        print('Cancelando a remoção do livro escolhido.....') 

def alterar_livro_info_view():
    print('\n')
    print('---------- Alterar informações de livro por id ----------')
    print('\n')

    livro_id = input('Digite o id do livro a ser modificado: ')

    if not livro_id.isdigit():
        print('Erro: Valor escrito é considerado invalido')
        return

    try:
        livro_id_int = int(livro_id)
    except ValueError as e:
        print(f'Erro: {e}')
        return
    
    try:
        livro = livro_por_id(livro_id_int)
    except ValueError as e:
        print(f'Erro: {e}')
        return
    
    if livro == None:
        print('O id digitado não existe!')
        return

    livro_detalhes_view(livro)

    escolha = input('Confirme que deseja modificar os dados do livro acima (S \ N): ').strip().upper() == 'S'

    if escolha:
        print('---------- Campos a modificar ----------')
        print('Caso não queria modificar algum campo somente de enter!')

        titulo = input('Novo título: ')
        autor = input('Novo autor: ')
        data_publicacao = input('Nova data de lançamento (YYYY-MM-DD): ')
        resumo = input('Novo resumo: ')
        numero_paginas = input('Novo número de páginas: ')

        if titulo.strip():
            livro.titulo = titulo
        
        if autor.strip():
            livro.autor = autor
        
        if data_publicacao.strip():
            livro.data_publicacao = data_publicacao
        
        if resumo.strip():
            livro.resumo = resumo
        
        if numero_paginas.strip():
            try:
                livro.numero_paginas = int(numero_paginas)
            except ValueError as e:
                print(f'Erro: {e} \n Cancelando a modificação.')
                return

        try:
            if input('Deseja confirmar as mudanças? Digite S para Confirmar e qualquer coisa para Cancelar\n >').strip().upper() == 'S':

                modificar_livro_por_id(livro)

                print("Livro modificado com sucesso!")
            else:
                print('Modificações canceladas, retornando ao menu principal.....')
        except ValueError as e:
            print(f'Erro: {e}')
            return

    else: 
        print('Confirmação Invalidada, fechando o sistema e voltando ao menu...')
        return
