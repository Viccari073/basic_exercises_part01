"""
Leia um valor de volume em metros cúbicos (m3) e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000*M, sendo L o volume em litros e M o volume em metros cúbicos.
"""

m3 = float(input('Qual o volume em metros cúbicos?'))
litros = 1000 * m3
print(f'O volume de {m3} corresponde à {litros} litros.')