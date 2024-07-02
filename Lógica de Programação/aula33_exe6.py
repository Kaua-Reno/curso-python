'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou  ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''
try:
    numero = input('Digite um número inteiro: ')
    numero = float(numero)
    if numero // 1 == numero:
        numero = int(numero)
        if numero % 2 == 0:
            print(f'o numero {numero} é par')
        else:
            print(f'o numero {numero} é ímpar')
    else:
        print('Você não escreveu um número inteiro')
except:
    print('Você não escreveu um número')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.
Bom dia: 0-11:59, Boa tarde: 12-17:59 e Boa noite: 18-23:59 
'''

hora = input('Digite que horas são agora: ')
hora_corrigida = hora.replace(":", ".")
hora_corrigida =  float(hora_corrigida)
if hora_corrigida >= 0 and hora_corrigida <= 11.59:
    print('Bom dia!')
elif hora_corrigida >= 12 and hora_corrigida <= 17.59:
    print('Boa tarde!')
else:
    print('Boa noite!')

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letra ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é de tamanho médio"; maior que 6 escreva "Seu nome é muito grande".
'''

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto")
elif tamanho_nome > 4 and tamanho_nome <=6:
    print("Seu nome é de tamanho médio")
else:
    print("Seu nome é grande")
