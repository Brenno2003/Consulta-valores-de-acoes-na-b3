from servico.utilidades import verificar_inteiro
from servico.acoes import cadastrar_acoes, relatorio_acoes, alterar_dados_acoes
from servico.preco import registrar_preco, relatorio_precos_diario
from servico.recomendado import relatorio_recomendados


#Meu para atendimento ao cliente
def meu_atendimento():
    while True:
        print('-' * 50)
        op = verificar_inteiro('''[1] Cadastrar acão
[2] Atualizar preço diario
[3] Relatorio de precos do dia
[4] Lista de recomendados
[5] Relatorios de acoes
[6] Alterar dados de acoes
[7] Sair

Escolha uma opção:''')
        print('-'*50)
        if op in (1, 2, 3, 4, 5, 6, 7):
            break
        else:
            print('\nOpção invalida, tente novamente')
    return op

#Atendimento
def atendimento():
    while True:
        op = meu_atendimento()
        match op:
            case 1:
                cadastrar_acoes()
            case 2:
                registrar_preco()
            case 3:
                relatorio_precos_diario()
            case 4:
                relatorio_recomendados()
            case 5:
                relatorio_acoes()
            case 6:
                alterar_dados_acoes()
            case 7:
                break



