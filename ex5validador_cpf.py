"""
Crie um código que deve receber um número 
de CPF do usuário, e seja capaz de confirmar 
se o CPF digitado é válido ou inválido.
"""
import re # expressão regular

entrada = input('CPF: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
) 

print(f'CPF enviado pelo usuário: {cpf_enviado_usuario}')

# Encontrar primeiro digito

nove_digitos = cpf_enviado_usuario[:9]

contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Encontrar segundo digito

dez_digitos = nove_digitos + str(digito_1)

contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(f'CPF gerado pelo cálculo: {cpf_gerado_pelo_calculo}')

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
   print(f'O CPF {entrada} é válido')
else:
    print(f'O CPF {entrada} é inválido')