"""
Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""

nota1 = float(input('A primeira nota é: '))
print(nota1)

nota2 = float(input('A segunda nota é: '))
print(nota2)

nota3 = float(input('A terceira nota é: '))
print(nota3)

nota4 = float(input('A quarta nota é: '))
print(nota4)

mediaAritmetica = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média aritmética é: {mediaAritmetica: .2f}')