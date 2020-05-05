"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""

print('Digite o primeiro valor: ')
valor1 = int(input())

print('Digite o segundo valor: ')
valor2 = int(input())

print('Digite o terceiro valor: ')
valor3 = int(input())

somaDosQuadrados = (valor1 * 2) + (valor2 * 2) + (valor3 * 2)
print(f'O quadrado da soma dos três valores é: {somaDosQuadrados}')