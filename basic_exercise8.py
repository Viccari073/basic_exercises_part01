"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

temperaturaKelvin = float(input('Qual a temperatura em graus Kelvin?'))

temperaturaCelsius = temperaturaKelvin - 273.15

print(f'A temperatura em Celsius é: {temperaturaCelsius: .2f} graus')