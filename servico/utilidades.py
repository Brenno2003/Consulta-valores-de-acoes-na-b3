from banco.crud_acoes import pesquisar_acao
from constantes import COD_ACAO


def inserir_nome():
    while True:
        nome = input('Qual o nome da empresa: ').upper()
        nome_verificado = verificar_nome(nome)
        if nome_verificado:
            break
        else:
            print('Erro: Nome muinto grande, tem que ter no maximo 100 e no minimo 1')
            print('Tente novamente')
    return nome_verificado

def verificar_nome(nome):
    if (0 < len(nome) <= 100):
        return nome
    else:
        return None

def inserir_nomenclatura():
    while True:
        nomenclatura = input('Qual a nomenclatura da empresa: ').upper()
        nomenclatura_verificado = verificar_nomenclatura(nomenclatura)
        if nomenclatura_verificado:
            break
        else:
            print('Erro: Nome muinto grande, tem que ter no maximo 100 e no minimo 1')
            print('Tente novamente')
    return nomenclatura_verificado

def verificar_nomenclatura(nomenclatura):
    if (0 < len(nomenclatura) <= 10):
        return nomenclatura
    else:
        return None

def validar_preco(preco):
    if ',' in preco:
        preco = preco.replace(',', '.')
    return float(preco)

def verificar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except Exception as erro:
            print(f"Erro: Digite um numero inteiro: {erro}")
    return num

def entrar_acao():
    while True:
        id_acao = verificar_inteiro("\nDigite o codigo do item: ")
        acao = pesquisar_acao(id_acao)
        if acao:
            break
        else:
            print("\nAção não existe")
    return acao[COD_ACAO]