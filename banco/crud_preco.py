from banco.conectar import conectar_banco, deconectar
from sqlalchemy import text
from datetime import date


def cadastrar_preco(preco, id_acao):
    sql = text('INSERT INTO bolsa.preco (preco, id_acao) VALUES (:preco, :id_acao)')
    try:
        session = conectar_banco()
        session.execute(sql, {'preco': preco, 'id_acao': id_acao})
        session.commit()
    except Exception as erro:
        print(f'Erro: {erro}')
        exit()
    finally:
        deconectar(session)

def consultar_preco_dia():
    data = date.today()
    sql = text(f" select distinct on (p.id_acao, DATE(p.data))p.id_preco, p.id_acao, a.nome,  DATE(p.data) as data, p.preco from bolsa.preco p inner join bolsa.acoes a on a.id_acao = p.id_acao where DATE(p.data) = :data order by p.id_acao, date(p.data), p.data desc")
    try:
        session = conectar_banco()
        preco = session.execute(sql, {"data": data}).fetchall()
        return preco
    except Exception as erro:
        print(f'Erro: {erro}')
    finally:
        deconectar(session)

def media_de_preco(id_acao):
    sql = text('''select id_acao, AVG(preco) AS media_preco
from(
    select distinct id_acao, DATE(data) AS dia, preco
    FROM bolsa.preco
) AS precos_unicos
where id_acao = :id_acao
group by id_acao
order by id_acao asc
''')
    try:
        session = conectar_banco()
        media_preco = session.execute(sql, {"id_acao": id_acao}).fetchone()
        return media_preco
    except Exception as erro:
        print(f'Erro: {erro}')
    finally:
        deconectar(session)