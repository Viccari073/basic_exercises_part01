"""
Leia um valor de comprimento em polegadas e apresnete-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""

p = float(input('Qual o comprimento em polegadas?'))
cm = p * 2.54
print(f'{p} polegadas corresponde à {cm: .2f} cm')