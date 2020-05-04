"""
Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * Pi/180, sendo G o ângulo em graus e R em radianos. Pi = 3.14.
"""

graus = float(input('Quantos graus tem o ângulo?'))
radianos = graus * 3.14 / 180
print(f'{graus} graus corresponde à {radianos: .2f} radianos.')