'''
Crie um programa que mostre a quantidade de vezes que
cada letra aparece e a letra mais repetida na frase.
'''

frase = input('Digite uma frase: ')

print(frase)
frase = frase.lower() # transforma todas as letras da frase em minúsculas
indices_na_frase = len(frase) # contagem de caracteres totais

separacao = '-' * 40
print(separacao)

print('* Contagem de letras:')

letra_mais_repetida = '' # essa variável irá receber a letra mais repetida na frase
qtd_letra_mais_repetida = 0 # e essa receberá a quantidade de vezes que a letra foi repetida

letras_ja_contadas = '' # variável que vai receber as letras no while, para evitar repetições

caracteres_para_ignorar = ' ', '.', '\n' # caracteres que não serão contados

i = 0 #index
while i < indices_na_frase:

    letra_atual = frase[i]

    if letra_atual in letras_ja_contadas: # processo de descartar letras já verificadas
        i += 1
        continue

    letras_ja_contadas += letra_atual
    
    if letra_atual in caracteres_para_ignorar:
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_letra_mais_repetida < qtd_atual:
        qtd_letra_mais_repetida = qtd_atual
        letra_mais_repetida = letra_atual

    print(f"'{letra_atual}' = {qtd_atual}")
    i += 1

print(separacao)

print(
    'A letra mais repetida na frase foi '
    f'"{letra_mais_repetida}", que apareceu '
    f'{qtd_letra_mais_repetida} vezes.'
)
