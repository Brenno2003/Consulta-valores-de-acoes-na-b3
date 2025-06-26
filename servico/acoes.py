from banco.crud_acoes import cadastrar_acao, consultar_acoes, update_dado_acoes
from servico.utilidades import inserir_nome, inserir_nomenclatura, verificar_inteiro, entrar_acao
from tabulate import tabulate

def meu_acoes():
    while True:
        print('-' * 50)
        op = verificar_inteiro('''[1] Alterar nome
[2] Alterar nomenclatura
[3] Sair

Escolha uma opção:''')
        print('-'*50)
        if op in (1, 2, 3):
            break
        else:
            print('\nOpção invalida, tente novamente')
    return op

def cadastrar_acoes():
    nome = inserir_nome()
    nomenclatura = inserir_nomenclatura()
    cadastrar_acao(nome, nomenclatura)

def relatorio_acoes():
    lista = consultar_acoes()
    headers = ["ID_ACAO", "NOME", "NOMENCLATURA"]
    tabela = tabulate(lista, headers=headers, numalign="right", stralign="left")
    print(tabela)

def alterar_nome(id_acao):
    coluna = 'nome'
    nome = inserir_nome()
    update_dado_acoes(coluna, id_acao, nome)

def alterar_nomenclatura(id_acao):
    coluna = 'nomenclatura'
    nomenclatura = inserir_nomenclatura()
    update_dado_acoes(coluna, id_acao, nomenclatura)

def alterar_dados_acoes():
    relatorio_acoes()
    id_acao = entrar_acao()
    while True:
        op = meu_acoes()
        match op:
            case 1:
               alterar_nome(id_acao)
            case 2:
                alterar_nomenclatura(id_acao)
            case 3:
                break