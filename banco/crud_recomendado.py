from banco.conectar import *
from sqlalchemy import text
from datetime import date

def cadastrar_recomendados(id_preco, id_nivel):
    sql = text('INSERT INTO bolsa.recomendados (id_preco, id_nivel) VALUES (:id_preco, :id_nivel)')
    try:
        session = conectar_banco()
        session.execute(sql, {'id_preco': id_preco, 'id_nivel': id_nivel})
        session.commit()
    except Exception as erro:
        print(f'Erro, cadastrar recomendados: {erro}')
    finally:
        deconectar(session)

def consultar_recomendados():
    data = date.today()
    sql = text(f'''select distinct a.nome, a.nomenclatura, p.preco, p."data", ndo.nome from bolsa.recomendados r
inner join bolsa.preco p on p.id_preco = r.id_preco
inner join bolsa.nivel_de_oportunidade ndo on ndo.id_nivel_de_oportunidade = r.id_nivel
inner join bolsa.acoes a on a.id_acao = p.id_acao
where p.data = :data''')
    try:
        session = conectar_banco()
        recomendados = session.execute(sql, {'data' :data}).fetchall()
        return recomendados
    except Exception as erro:
        print(f'Erro: {erro}')
    finally:
        deconectar(session)