from datetime import datetime
from datetime import timedelta
from time import sleep
from projeto_1.library import interface
from projeto_1.library import dados
from projeto_1.library import respostas

interface.cabeçalho('SEU CICLO')  # cabeçalho com o nome do programa.

while True:
    dados.nome('Para começarmos, digite seu nome: ') # coleta o nome do usuário.

    interface.apresentação() # apresentação do objetivo do programa personalizada com o nome do usuário.

    # Coleta dos dados principais para o funcionamento do programa.
    data_última = dados.formataData('Quando foi sua última menstruação? [dd-mm-aaaa]: ')
    ciclo_completo = dados.ciclo('Quantos dias seu ciclo costuma ter? [de uma menstruação até a outra] ')
    período_menstrual = dados.ciclo('Quantos dias você fica menstruada? ')

    # Organiza Variáveis - Datas(datetime)
    hoje = datetime.now()
    próximo_ciclo = data_última + timedelta(days=ciclo_completo)
    próximo_ciclo_formatado = datetime.strftime(próximo_ciclo, '%d-%m-%Y')

    # Organiza Variáveis - Contagem de dias(days ou int)
    dias_do_ciclo = hoje - data_última

    # Organiza variáveis por período.
    menstruação = período_menstrual
    pré_ovulatório = ciclo_completo - 16
    ovulação = ciclo_completo - 14
    fértil = ciclo_completo - 12
    ppm = ciclo_completo - 7
    tpm = ciclo_completo

    # Tempo de carregamento antes de mostrar as respostas.
    print(interface.linha())
    interface.carregando()

    # Inicia as mensagens que serão mostradas na tela.
    print(interface.linha())
    sleep(1)
    print(f'Você está no \033[35m{dias_do_ciclo.days}º\033[m dia do seu ciclo.')
    print()

    # Condicionais que retornam respostas de acordo com as variáveis.
    if dias_do_ciclo.days < menstruação:
        respostas.menstruação()
    elif dias_do_ciclo.days < pré_ovulatório:
        respostas.pré_ovulatório()
    elif dias_do_ciclo.days < fértil:
        respostas.fértil()
    elif dias_do_ciclo.days < ppm:
        respostas.ppm()
    elif dias_do_ciclo.days < tpm:
        respostas.tpm()
    elif dias_do_ciclo.days > ciclo_completo:
        atraso = (ciclo_completo - dias_do_ciclo.days) * -1
        print(f'Atraso de {atraso} dias.')
        respostas.atraso()

    # Mensagens padrão ao término da condição programada.
    print(f'\nSua próxima menstruação deve acontecer em: \033[35m{próximo_ciclo_formatado}\033[m ')
    respostas.msg_final()

    # Menu para escolher continuar no programa ou sair.
    resposta = interface.menu(['Fazer de novo!', 'Sair'])
    if resposta > 2 or resposta < 1:
        interface.erro()
        resposta = interface.menu(['Fazer de novo!', 'Sair'])
    if resposta == 2:
        print('Saindo do sistema'.center(60))
        print()
        interface.carregando()
        print()
        print('Até a próxima!👋'.center(60))
        print(interface.linha())
        break
