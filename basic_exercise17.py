"""
Leia um valor de comprimeto em centímetro e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C / 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""

cm = float(input('Qual o comprimento em centímeto?'))
p = cm / 2.54
print(f'{cm} cm corresponde à {p: .2f} podelgadas.')

