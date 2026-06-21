import os

restaurantes = [{'nome':'Pizza Hut', 'categoria':'Pizza', 'ativo':True},
                {'nome':'LifeBox', 'categoria':'Hambúrguer', 'ativo':True},
                {'nome':'QG', 'categoria':'Comida', 'ativo':False},
                {'nome':'Sushi', 'categoria':'Japonesa', 'ativo':True}]

def finalizar_app():
    ''' Essa função é responsável por finalizar o app '''
    os.system('cls')
    print('Finalizando o app')

def voltar_ao_menu():
    ''' Essa função é responsável por voltar ao menu '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    ''' Essa função é respon'savel por exibir o subtítulo '''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    ''' Essa função é responsável para voltar ao menu caso receba alguma opção inválida '''
    print('Opção inválida!\n')
    voltar_ao_menu()

def exibir_nome_programa():
    ''' Essa função é responsável por exibir o nome do programa '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    ''' Essa função é responsável por exibir as opções para o usuário '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input('Digite a categoria do restaurante: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    ''' Essa função é responsável por listar o restaurantes '''
    exibir_subtitulo('Lista de restaurantes:')

    print(f'{'Nome Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()

def alternar_estado_do_restaurante():
    ''' Essa função é responsável por alternar o estado do restaurante '''
    exibir_subtitulo('Alternando Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False 

    # Conferindo se o restaurante foi encontrado e se for, vai alternar o estado do mesmo 
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] == True else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário
    
    Output:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Essa função é responsável por realizar o programa por completo '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()