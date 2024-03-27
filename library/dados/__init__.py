def nome(txt):
    """
    -> Solicita o nome do usuário e retorna mensagem personalizada.
    :param txt: nome digitado pelo usuário
    :return: mensagem personalizada com o nome do usuário
    """
    from projeto_1.library.interface import cores
    from projeto_1.library.interface import linha
    ok = False
    while True:
        try:
            nome = str(input(f'{cores(5)}{txt}{cores(0)}')).strip().upper()
            print(linha())
            if nome.isalpha():
                ok = True
                print(f'Olá, {cores(5)}{nome}{cores(0)}! É um prazer te conhecer!'.center(65))
                break
            else:
                print(f'{cores(1)}Ops! Parece que houve um erro.\n'
                      f'Por favor, digite apenas letras.{cores(0)}')
                print(linha())
                ok = False
        except (ValueError, TypeError):
            print(f'{cores(1)}Ops! Parece que houve um erro.\n'
                      f'Por favor, digite apenas letras.{cores(0)}')
            print(linha())


def formataData(txt):
    """
    -> String Parse Time: analisa a string e extrai dados datetime
    no formato Brasileiro (dia-mês-ano).
    :param data: objeto string a ser formatado.
    :return: objeto datetime em formatado BR: dia-mês-ano.
    """
    from datetime import datetime
    from projeto_1.library.interface import cores, linha
    ok = False
    while True:
        d = (str(input(txt))).strip().replace('/', '-').replace('.', '-')
        try:
            data = datetime.strptime((d), '%d-%m-%Y')
            ok = True
            return data
        except KeyboardInterrupt:
            print(f'{cores(1)}O usuário interrompeu o programa.\n'
                  f'{cores(0)}VOLTE SEMPRE!.')
            print(linha())
            ok = True
            break
        except Exception as e:
            print(f'{cores(1)}ERRO: Parece que a houve um problema com a data.\n'
                  f'Por favor, tente novamente.{cores(0)}')
            print(linha())
            ok = False

def ciclo(msg):
    """
    -> Recebe dados int sobre o ciclo do usuário e trata erros se
     necessário.
    :param msg: quantidade de dias relacionada à pergunta feita.
    :return: quantidade de dias no formato int.
    """
    ok = False
    while True:
        ciclo = input(msg)
        try:
            if ciclo.isnumeric():
                ok = True
                return int(ciclo)
        except (TypeError, ValueError):
            print(f'{cores(1)}ERRO: Parece que a houve um problema com a data.\n'
                  f'Por favor, tente novamente.{cores(0)}')
            print(linha())
            ok = False
        except KeyboardInterrupt:
            print(f'{cores(1)}O usuário interrompeu o programa.\n'
                  f'{cores(0)}VOLTE SEMPRE!.')
            print(linha())
            ok = True
            break
