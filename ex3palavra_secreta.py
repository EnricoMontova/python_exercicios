"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# Apresentação do jogo
print(' * JOGO DA ADIVINHAÇÃO *')

palavra_secreta = 'xadrez' 

# Varáveis que serão usadas no loop principal
palpite_certo = ''
palavra_exibida = ''
tentativas = 0

# loop para formar a palavra com asteríscos antes do jogo começar
asteriscos = ''

for letra in palavra_secreta:
    asteriscos += '*'
print(f'Adivinhe a palavra secreta: {asteriscos}')

# loop principal
while palavra_exibida != palavra_secreta:
    
    palpite = input('Digite uma letra: ').lower() # Evitar problemas caso o jogador digitar com o caps ligado

    if len(palpite) != 1: # confirmação de que o jogador digitou apenas uma letra
        print('Digite apenas uma letra!')
        continue

    if palpite in palavra_secreta: # armazenamento de palpites certos em uma variável
        palpite_certo += palpite
    
    palavra_exibida = '' #variável para o loop interno de exibição da palavra secreta 

    # loop interno
    for letra in palavra_secreta:
        if letra in palpite_certo:
            palavra_exibida += letra
        else:
            palavra_exibida += '*'
    
    print(palavra_exibida)
    tentativas += 1

# Fim de jogo
print('Parabéns, você ganhou!!')

print(
    f'A palavra secreta era "{palavra_secreta}".\n'
    f'Você teve o total de {tentativas} tentativas.'
)