"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""

valorHora = float(input('Qual o valor/hora de trabalho? R$'))
horasTabalhadas = float(input('Quantas horas tabalhadas no mês?'))

bruto = valorHora * horasTabalhadas
bonus = bruto * 10/100
liquido = bruto + bonus

print(f'O salário correspondente à {horasTabalhadas}h, mais a bonificação de 10% é R$ {liquido: .2f}.')

