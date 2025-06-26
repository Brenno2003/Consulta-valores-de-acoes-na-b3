from constantes import PRECO_ACAO, COD_PRECO, COD_ACAO
from banco.crud_preco import consultar_preco_dia, media_de_preco
from banco.crud_recomendado import cadastrar_recomendados, consultar_recomendados
from tabulate import tabulate


def nivel_recomendado(acao):
    preco = float(acao[4])
    media = media_de_preco(acao[1])[PRECO_ACAO]
    preco_baixo = float(media) * 0.75
    nivel = 0
    if media == preco:
        nivel = 1
    elif preco_baixo < preco < media:
        nivel = 2
    elif preco_baixo >= preco:
        nivel = 3
    return nivel

def registrar_recomendados(acoes):
    for acao in acoes:
        nivel = nivel_recomendado(acao)
        if nivel > 0:
            cadastrar_recomendados(acao[COD_PRECO], nivel)

def recomendados():
    acoes = consultar_preco_dia()
    registrar_recomendados(acoes)

def relatorio_recomendados():
    lista = consultar_recomendados()
    headers = ["NOME", "NOMENCLATURA", "PREÇO", "DATA", "NIVEL_OPORTUNIDADE"]
    tabela = tabulate(lista, headers=headers, numalign="right", stralign="left")
    print(tabela)


