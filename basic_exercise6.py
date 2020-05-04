"""
Leia a temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""


celsius = float(input('Qual a temperatura em Celsius?'))

Fahrenheit = celsius * (9.0/5.0) + 32.0

print(f'A temperatura em Fahrenheit é de: {Fahrenheit} graus.')