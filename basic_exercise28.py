"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.
"""

valor = float(input('Qual o valor do produto? R$'))
desconto = valor - (valor * 12 / 100)

print(f'O valor de R${valor: .2f} com 12% de desconto é R${desconto: .2f}.')
