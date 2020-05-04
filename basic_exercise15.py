"""
Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180 / Pi, sendo o ângulo em graus e R em radianos e Pi = 3.14
"""

R = float(input('Quanto mede, em radianos, o ângulo?'))
G = R * 180 / 3.14
print(f'Um ângulo com {R} radianos corresponde à {G: .2f} graus')

