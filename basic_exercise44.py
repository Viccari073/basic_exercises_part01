"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""

altDegrau = float(input('Qual a altura, em centímetros, do degrau?'))
altFinal = float(input('Qual a altura, em centímetros, desejada?'))

qtdtDegraus = altFinal/altDegrau

print('A quantidade de degraus para se alcançar {:.0f}cm de altura é de {:.0f} degraus.'.format(altFinal, qtdtDegraus))


