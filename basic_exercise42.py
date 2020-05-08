"""
Receba um salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário
tem uma gratificação de 5% sobte o salário-base. Além disso, ele paga 7% de imposto sobre o salário base.
"""

base = float(input('Qual o salário base? R$'))
gratificacao = base * 5/100
imposto = base * 7/100
liquido = base + gratificacao - imposto

print(f'O salário líquido é R${liquido: .2f}.')
