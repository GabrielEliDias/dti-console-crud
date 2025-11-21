from data.database import inicializar_banco
from views.livro_view import listar_livros_view, registrar_livro_view, dados_livro_view, deletar_livro_view

def main():

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
            ...
        elif escolha == '5':
            deletar_livro_view()
        elif escolha == '6':
            print('Fechando o programa.....')
            return
        else: 
            print("Comando não identificado, por favor insira o comando novamente.")
            continue

if __name__ == "__main__":
    main()