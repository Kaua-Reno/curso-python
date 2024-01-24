# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3
#  k a u a
# -4-3-2-1
nome = 'Kauã'
print(nome[2])
print(nome[-3])
print('uã' in nome)
print('zero' in nome)
print(10 * '-')
print('uã' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')