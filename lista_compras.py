'''
Faça uma lista de comprar com listas.

O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com
erros de índices inexistentes na lista.
'''

lista = []

while True:

    comando = input(
        '[1] inserir, [2] apagar, [3] listar, [4] Sair: '
    )

    try:       
        comando = int(comando)
                        
        if comando == 1:
            inserir = input('Digite o que deseja inserir na lista: ')
            lista.append(inserir.capitalize())
            print(lista)

        elif comando == 2:
            if lista == []:
                print('Não há valores para apagar na lista!')
            
            else:        
                apagar = input('Digite qual item da lista deseja apagar: ')
                apagar = apagar.capitalize()
                
                if apagar in lista:
                    apagar = lista.index(apagar)
                    del lista[apagar]
                    print(lista)

                else:
                    print('Esse valor não está na lista.')

        elif comando == 3:
            if lista == []:
                print('Não há itens na lista ainda.')
            
            else:
                itens_na_lista = range(len(lista))

                for item in itens_na_lista:
                    print(f'{item + 1}. {lista[item]}')


        elif comando == 4:
            print('Finalizando o programa.')
            break

        else:
            print('Por favor, digite um comando válido.')

    except ValueError:
        print('Por favor, digite um comando válido.')

if lista:           
    print('Assim ficou sua lista:')

    itens_na_lista = range(len(lista))

    for item in itens_na_lista:
        print(f'{item + 1}. {lista[item]}')

else:
    print('A lista está vazia.')