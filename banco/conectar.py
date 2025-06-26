from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constantes import BANCO_DE_DADOS

def conectar_banco():
    try:
        engine = create_engine(f'postgresql+psycopg2://postgres:1234@localhost:5432/{BANCO_DE_DADOS}')
        session = sessionmaker(bind=engine)()
    except Exception as erro:
        print(f'Erro ao acessar o banco: {erro}')
        exit()
    return session

def deconectar(session):
    if session:
        session.close()