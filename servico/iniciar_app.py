from servico.utilidades import verificar_inteiro

def menu_inicar():
    while True:
        op = verificar_inteiro('''[1]Iniciar Atendimento\n[2]Finalizar Atendimento

Escolha uma opção:''')
        if op in (1, 2):
            break
        else:
            print('Opção invalida, tente novamente')
    return op