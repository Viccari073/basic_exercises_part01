"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
123
321
"""

num = input('Digite um número de três dígitos:')

print(f'O número {num} invertido é: {num[::-1]}')
