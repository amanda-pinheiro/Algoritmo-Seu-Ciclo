from projeto_1.library.interface import cores
from time import sleep


def msg_final():
    """
    -> Mostra mensagem padrão ao final de cada condição do programa
    principal.
    :return: mensagem padrão de finalização.
    """
    print()
    print(f'Mas lembre-se, o mais importante é utilizar'
          f' esta ferramenta para \nse auto-conhecer, pois'
          f' {cores(5)}seu ciclo{cores(0)} é único ❤️')
    print('\nEspero ter ajudado!')
    print(f'\n{cores(1)}Lembrete:')
    print(f'\n{cores(1)}Se seu ciclo for irregular, fique atenta!\n'
          f'Pode haver alterações em relação ao seu período fértil,\n'
          f'ou outras questões de saúde. Consulte um médico.'
          f'{cores(0)}')
    sleep(2)

def menstruação():
    """
    -> Mostra mensagem padrão para a condição 'menstruação' do programa
    principal.
    :return: mensagem padrão para a condição 'menstruação'.
    """
    sleep(1)
    print(f'🟣 Fase: {cores(5)}folicular{cores(0)}\n'
          f'🟣 Período:{cores(5)}menstrual{cores(0)}\n'
          f'🟣 Duração comum: {cores(5)}1{cores(0)} a'
          f'{cores(5)}6{cores(0)} dias.\n'
          f'🟣 Idéias para o seu momento: Como é comum estar menos\n'
          f'disposta durante este período, pegue leve com você,\n'
          f'faça exercícios moderados e hidrate-se.\n'
          f'Se focar em tarefas mais introspectivas pode ser bastante proveitoso.')

def pré_ovulatório():
    """
    -> Mostra mensagem padrão para a condição 'pré-ovulatória' do programa
    principal.
    :return: mensagem padrão para a condição 'pré-ovulatório'.
    """
    sleep(1)
    print(f'🟣 Fase: {cores(5)}folicular{cores(0)}\n'
          f'🟣 Período:{cores(5)}pré-ovulatório{cores(0)}\n'
          f'🟣 Duração comum: {cores(5)}1{cores(0)}{cores(5)}3{cores(0)} dias'
          f'após a menstruação, pode variar de ciclo para ciclo.\n'
          f'🟣 Idéias para o seu momento: Neste período é comum\n'
          f'estar mais disposta.\n'
          f'Pode ser bacana tentar coisas novas, aumentar a intensidade de\n'
          f'exercícios, entre outras possibilidades.\n'
          f'A criatividade também pode estar em alta! Aproveite seu momento.')


def fértil():
    """
    -> Mostra mensagem padrão para a condição 'período fértil' do programa
    principal.
    :return: mensagem padrão para a condição 'período fértil'.
    """
    sleep(1)
    print(f'🟣 Fase: {cores(5)}folicular{cores(0)}\n'
          f'🟣 Período:{cores(5)}fértil{cores(0)}\n'
          f'🟣 Duração comum: {cores(5)}5{cores(0)} a '
          f'{cores(5)}7{cores(0)} dias.\n'
          f'🟣 Sinais: Observar seu muco cervical.\n'
          f'Provavelmente, você encontrará na sua calcinha\n'
          f'um líquido viscoso transparente similar à clara de ovo.\n'
          f'🟣 Idéias para o seu momento: Neste período é comum \n'
          f'estar mais disposta. Pode ser um bom momento para\n'
          f'tentar coisas novas, e aproveitar a libido alta com os\n'
          f'cuidados necessários, claro.\n'
          f'A criatividade também pode estar em alta! Aproveite seu momento.')


def ppm():
    """
    -> Mostra mensagem padrão para a condição 'ppm' do programa
    principal.
    :return: mensagem padrão para a condição 'ppm'.
    """
    sleep(1)
    print(f'🟣 Fase: {cores(5)}lútea{cores(0)}\n'
          f'🟣 Período: {cores(5)}pré-menstrual{cores(0)}\n'
          f'🟣 Duração comum: {cores(5)}3{cores(0)} a '
          f'{cores(5)}4{cores(0)} dias.\n'
          f'🟣 Idéias para o seu momento: É comum que a força\n'
          f'física se altere e diminua gradativamente por conta\n'
          f'da queda brusca de hormônios neste período.\n'
          f'As atividades físicas podem ser moderadas e o humor\n'
          f'também pode sofrer mais alterações.\n'
          f'Neste momento, podem caber atividades de cunho mais\n'
          f'reflexivo e eventuais recolhimentos se necessário.')


def tpm():
    """
    -> Mostra mensagem padrão para a condição 'tpm' do programa
    principal.
    :return: mensagem padrão para a condição 'tpm'.
    """
    sleep(1)
    print(f'🟣 Fase: {cores(5)}folicular{cores(0)}\n'
          f'🟣 Período:{cores(5)}tensão pré-menstrual{cores(0)}\n'
          f'🟣 Duração comum: {cores(5)}7{cores(0)} a '
          f'{cores(5)}10{cores(0)} dias.\n'
          f'🟣 Idéias para o seu momento: É comum que a força\n'
          f'física seja menor neste período por conta da queda brusca\n'
          f'de hormônios, assim como apresentar alguns desconfortos\n'
          f'físicos como dores de cabeça, cólicas e maior retenção de líquido.\n'
          f'As atividades físicas podem ser moderadas e o humor\n'
          f'também pode sofrer mais alterações.\n'
          f'Neste momento, podem caber atividades de cunho mais\n'
          f'reflexivo e eventuais recolhimentos se necessário.')


def atraso():
    """
    -> Mostra mensagem padrão para a condição 'atraso' do programa
    principal.
    :return: mensagem padrão para a condição 'atraso'.
    """
    sleep(1)
    print()
    print(f'Ops! Parece que sua menstruação está {cores(1)}atrasada{cores(0)}.\n'
          f'Se existir a possibilidade de gravidez ou outras questões\n'
          f'sobre a sua saúde, procure um médico.\n')
