"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obitda pela equação: hipotenusa = raiz quadrada a**2 + b**b.
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
Imprimao resultado dessa operação.
"""

a = int(input('Qual o valor de a?'))
b = int(input('QUal o valor de b?'))
h = (a**2 + b**2)**(1/2)

print(f'O valor da hipotenusa é {h: .2f}.')