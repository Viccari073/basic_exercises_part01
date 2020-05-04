"""
Leia uma distância em quilômetros e apresente-a convertida em milhas.
A fórmula de conversão é: M = K/1.61, sendo K a distância em quilômetros e M em milhas.
"""

K = float(input("Qual a distância em quilômetros?"))
M = K / 1.61
print('A distância de {0} quilômetros correspodne à {1: .2f} milhas'.format(K, M))