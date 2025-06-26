from servico.iniciar_app import menu_inicar
from servico.atendimento import atendimento

if __name__ == '__main__':
    while True:
        op = menu_inicar()
        match op:
            case 1:
                atendimento()
            case 2:
                print('Sessao finalizada')
                break
''':(:'''