from banco.raspagem_de_dados import pegar_perco, acessar_web
from banco.crud_preco import cadastrar_preco, consultar_preco_dia
from constantes import *
from banco.crud_acoes import consultar_acoes
from servico.utilidades import validar_preco
from tabulate import tabulate
from servico.recomendado import recomendados

def presquisar_preco(driver, acao):
    preco = pegar_perco(driver ,acao[NOMENCLATURA_ACAO])
    preco_formatado = validar_preco(preco)
    return preco_formatado

def inserir_preco_lista(driver, acao, lista_acoes_precos):
    preco = presquisar_preco(driver, acao)
    print(preco)
    id_acao = int(acao[COD_ACAO])
    lista_acoes_precos.append([id_acao, preco])

def lista_preco():
    acoes = consultar_acoes()
    driver = acessar_web()
    lista_acoes_precos = []
    try:
        for acao in acoes:
            inserir_preco_lista(driver, acao, lista_acoes_precos)
    except Exception as erro:
        print(f'Erro: {erro}')
        lista_acoes_precos = []
    finally:
        driver.quit()
        return lista_acoes_precos

def inserir_preco_tabela(acao):
    id_acao = int(acao[COD_ACAO])
    preco = acao[PRECO_ACAO]
    cadastrar_preco(preco, id_acao)

def registrar_preco():
    acoes = lista_preco()
    for acao in acoes:
        inserir_preco_tabela(acao)
    recomendados()

def relatorio_precos_diario():
    precos = consultar_preco_dia()
    headers = ["Codigo", "Nome", "Data", "Preço"]
    tabela = tabulate(precos, headers=headers, numalign="right", stralign="left")
    print(tabela)
