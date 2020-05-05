"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

n = int(input('Digite um número: '))
s = int(((n * 3) + 1) + ((n * 2) -1))
print(f'{s}')