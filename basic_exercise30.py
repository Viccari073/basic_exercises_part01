"""
A importância de R$ 780.000,00 será divida entre três ganhadores de um concurso. Sendo que da quantida total:
- O primeiro ganhador receberá 46%;
- O segundo ganhador receberá 32%;
_ O terceiro ganhador receberá o restante.

Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

premio = 780_000.00

ganhadorUm = premio * 46 /100
ganhadorDois = premio * 32 /100
ganhadorTres = premio - (ganhadorUm + ganhadorDois)

print(f'O primeiro ganhador receberá R${ganhadorUm: .2f}.')
print(f'O segundo ganhador receberá R${ganhadorDois: .2f}.')
print(f'O terceiro ganhador receberá R${ganhadorTres}.')

