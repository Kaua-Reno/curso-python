'''Calculadora com while'''
'''Ações: Adição, Subtração, Multiplicação, Divisão'''

while True:
    calculo = input('Qual operação você deseja realizar ?[1]adição - [2]subtração - [3]multiplicação - [4]divisão: ')
    conta = 0
    x = 1
    if calculo == '1':
        numero = int(input(f'Digite o {x}º número: '))
        x = x + 1
        numero2 = int(input(f'Digite o {x}º número: {numero} + '))
        conta = conta + numero + numero2
        while True:
            print(f"Esse é o resultado atual da sua adição: {conta}")
            mais_numeros = input('Você deseja somar mais números? [s]im/[n]ão: ' ).lower()
            if mais_numeros == 'n':
                break
            else:
                x = x + 1
                numero = int(input(f'Digite o {x}º número: {conta} + '))
                conta = conta + numero
        break
    elif calculo == '2':
        numero = int(input(f'Digite o {x}º número: '))
        x = x + 1
        numero2 = int(input(f'Digite o {x}º número: {numero} - '))
        conta = numero - numero2
        while True:
            print(f"Esse é o resultado atual da sua subtração: {conta}")
            mais_numeros = input('Você deseja somar mais números? [s]im/[n]ão: ' ).lower()
            if mais_numeros == 'n':
                break
            else:
                x = x + 1
                numero = int(input(f'Digite o {x}º número: {conta} - '))
                conta = conta - numero
        print(conta)
        break
    elif calculo == '3':
        conta = 1
        numero = int(input(f'Digite o {x}º número: '))
        x = x + 1
        numero2 = int(input(f'Digite o {x}º número: {numero} * '))
        conta = conta * numero * numero2
        while True:
            print(f"Esse é o resultado atual da sua multiplicação: {conta}")
            mais_numeros = input('Você deseja somar mais números? [s]im/[n]ão: ' ).lower()
            if mais_numeros == 'n':
                break
            else:
                x = x + 1
                numero = int(input(f'Digite o {x}º número: {conta} * '))
                conta = conta * numero
        break
    elif calculo == '4':
        conta = 1
        numero = float(input(f'Digite o {x}º número: '))
        x = x + 1
        numero2 = float(input(f'Digite o {x}º número: {numero} / '))
        conta = numero / numero2 / conta
        while True:
            print(f"Esse é o resultado atual da sua divisão: {conta}")
            mais_numeros = input('Você deseja somar mais números? [s]im/[n]ão: ' ).lower()
            if mais_numeros == 'n':
                break
            else:
                x = x + 1
                numero = int(input(f'Digite o {x}º número: {conta} / '))
                conta = conta / numero
        break
    else:
        print('Você não digitou nenhuma das opções')
print(conta)