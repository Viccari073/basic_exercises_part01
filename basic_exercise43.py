"""
Escreva um programa de ajuda para vendedores. A partir de um vlaor lido, mostre:
 - o total a pagar com desconto de 10%;
 - o total de cada parcela, no parcelamento em 3x sem juros;
 - a comissãso do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
 - a comissão do vendedor, no caso da venda pacelada (5% sobre o valor total).
"""

valorVenda = float(input('Qual o valor ro produto? R$'))

descVista = valorVenda - (valorVenda * 10/100)
comVista = descVista * 5/100
parcelado = valorVenda / 3
comParc = valorVenda * 5/100

print(f'O valor do produto é R${valorVenda: .2f}.')
print(f'O total a pagar com 10% de desconto é R${descVista: .2f} e a comissão do vendedor será de R${comVista: .2f}.')
print(f'Se parcelado em 3x, cada parcela será de R${parcelado: .2f} e a comissão do vendedor será de R${comParc: .2f}.')
