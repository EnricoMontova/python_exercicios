'''Calculadora com while'''

while True: # ciclo infinito
    numero_1 = input('Número 1:')
    numero_2 = input('Número 2:')
    operador = input('Operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1) # converte para float
        num_2_float = float(numero_2)
        numeros_validos = True # se convertível, números digitados conforme o planejado
    except:
        numeros_validos = None # número inválido se não convertível

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    soma = num_1_float + num_2_float
    subtracao = num_1_float - num_2_float
    divisao = num_1_float / num_2_float
    multiplicacao = num_1_float * num_2_float

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {soma}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {subtracao}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {divisao}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {multiplicacao}')
    else:
        print('Isso não é possível') # na teoria, é impossível se chegar a esse else, por causa de toda a validação código acima

    sair = input('Digite [s] se deseja sair. \n(Para repetir, clique na tecla enter):\n').lower().startswith('s')

    if sair is True:
        break