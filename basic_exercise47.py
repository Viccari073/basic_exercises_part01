"""
Leia um número de 4 dígitos de (1000 a 9999) e imprima 1 dígito por linha.

# Ou pode-se transformar o número em uma string e trabalhar com módulos:
num = int(input('Informe um número de 4 dígitos:')
num = str(num)
print(f'Número de 4 dígitos: {num}')
print(f'{num[3]}') # número na posição 3
print(f'{num[2]}') # número na posição 2
print(f'{num[1]}') # número na posição 1
print(f'{num[0]}') # número na posição 0

"""

num = int(input('Informe um número de 4 dígitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Número de 4 dígitos: {num}')
print(f'{u}')
print(f'{d}')
print(f'{c}')
print(f'{m}')




