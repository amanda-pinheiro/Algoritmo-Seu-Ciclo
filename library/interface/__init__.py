def leiaint(msg):
    """
    -> Lê valor inserido na tela e retorna int ou mensagem de erro.
    :param msg: mensagem que será inserida na chamada da função.
    :return: se a mensagem digitada for um número inteiro, ele é o return.
    Se não, o return é uma mensagem de erro.
    """
    ok = False
    valor = 0
    while True:
       n = str(input(msg))
       try:
           valor = int(n)
           ok = True
       except (TypeError, ValueError):
           print(f'{cores(1)}ERRO! Por favor, digite apenas 1 ou 2.{cores(0)}')
           continue
       except (KeyboardInterrupt):
           print(f'{cores(1)}Entrada de dados interrompida pelo usuário.{cores(0)}')
           return 0
       else:
           return valor


def erro():
    """
    -> Mensagem de erro padrão
    :return: print da mensagem de erro padrão.
    """
    print(f'{cores(1)}ERRO! Por favor, digite apenas 1 ou 2.{cores(0)}')

def linha(tam=60):
    return '-' * tam

def cores(num):
    """
    -> Chamada das cores por meio de tupla.
    :param num: o índice da cor na tupla.
    :return: o código pada a cor desejada.
    """
    c = ('\033[m',  # 0 - sem cores
         '\033[0;31m',  # 1 - vermelho
         '\033[0;32m',  # 2 - verde
         '\033[0;33m',  # 3 - amarelo
         '\033[0;34m',  # 4 - azul
         '\033[0;35m',  # 5 - roxo
         '\033[7m',  # 6 - branco
         )
    return c[num]

def cabeçalho(txt):
    """
    -> Padroniza os cabeçalhos do programa
    :param txt: mensagem a ser exibida no cabeçalho.
    :return: print do cabeçalho completo.
    """
    from time import sleep
    print(linha())
    print(f'{cores(5)}{txt}{cores(0)}'.center(65))
    print(linha())
    sleep(0.7)


def apresentação():
    """
    -> Apresenta o objetivo do programa
    :return: print do objetivo do programa e
    próximo passo.
    """
    from time import sleep
    from projeto_1.library import dados
    print(f'Vamos descobrir mais sobre o momento do ciclo menstrual?'.center(65))
    print()
    print('Para isso, precisarei te fazer algumas perguntas.'.center(65))
    print('Então vamos começar...'.center(65))
    carregando()
    print()
    sleep(0.5)
    print(linha())


def menu(lista):
    """
    -> Opções ao fim da execução do programa
    :param lista: opções digitadas na chamada da função.
    :return: seguimento do programa com a opção escolhida
     baseada no menu.
    """
    c = 1
    cabeçalho('Agora você pode escolher...')
    for item in lista:
        print(f'{cores(4)}{c}{cores(0)} - {item}')
        c += 1
    print(linha())
    opc = leiaint(f'{cores(5)}Sua opção: {cores(0)}')
    print(linha())
    return opc

def carregando():
    """
    -> Intervalo de tempo para mostrar informações.
    :return: print com o símbolo '*' por 3 segundos
    representando o carregamento de informações.
    """
    from time import sleep
    for p in range(0, 3):
        print(f'{cores(5)}*{cores(0)}'.center(30), end='')
        sleep(0.7)
    print()
