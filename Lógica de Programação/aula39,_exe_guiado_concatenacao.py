"""
Iterando string com while
"""

#.......01234567891011
nome = 'Kauã Gustavo' #Iteráveis
#.......121110987654321
print(nome[-12])
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

contador = 0
novo_nome = ''
while contador < tamanho_nome:
    letra = '*' + nome[contador]
    novo_nome += letra
    contador += 1
novo_nome += '*'
print(novo_nome)