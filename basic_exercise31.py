"""
Uma empresa contrata um encanador a R$ 30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá
ser paga, sabendo-se que são descontaos 8% para imposto de renda.
"""

diasTrabalhados = float(input('Quantos dias de trabalho?'))

valorDia = float(30.00)
bruto = diasTrabalhados * valorDia
desconto = float(bruto * 8/100)
liquido = bruto - desconto

print(f'O valor liquido, descontado o IR é R$ {liquido: .2f}.')

