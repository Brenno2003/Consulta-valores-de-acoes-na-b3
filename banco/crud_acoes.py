from banco.conectar import *
from sqlalchemy import text

def cadastrar_acao(nome, nomenclatura):
    sql = text('INSERT INTO bolsa.acoes (nome, nomenclatura) VALUES (:nome, :nomenclatura)')
    try:
        session = conectar_banco()
        session.execute(sql, {'nome': nome, 'nomenclatura': nomenclatura})
        session.commit()
    except Exception as erro:
        print(f'Erro: {erro}')
    finally:
        deconectar(session)

def consultar_acoes():
    sql = text(f"SELECT * FROM bolsa.acoes")
    try:
        session = conectar_banco()
        acoes = session.execute(sql).fetchall()
        return acoes
    except Exception as erro:
        print(f'Erro: {erro}')
    finally:
        deconectar(session)

def pesquisar_acao(id_acao):
    sql = text(f"SELECT * FROM bolsa.acoes WHERE id_acao = :id_acao")
    acao = None
    try:
        session = conectar_banco()
        acao = session.execute(sql, {'id_acao': id_acao}).fetchone()
    except Exception as erro:
        print(f'Erro ao verificar acao: {erro}')
    finally:
        deconectar(session)
    return acao

def update_dado_acoes(coluna, id_acao, alteracao):
    sql = text(f"update bolsa.acoes set {coluna} = :alteracao where id_acao = :id_acao")
    try:
        session = conectar_banco()
        session.execute(sql, {'alteracao': alteracao, 'id_acao': id_acao})
        session.commit()
    except Exception as erro:
        print(f'Erro: {erro}')
    finally:
        deconectar(session)