'''
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
'''

salario = float(input("Qual seu salário? R$"))
aumento = salario + (salario * 25 / 100)

print(f'Seu salário com 25% de aumento fica: R${aumento: .2f}.')