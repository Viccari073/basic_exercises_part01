"""
Leia um número inteiro em segundos e imprima-o em horas, minutos e segundos.
"""

segundosTotal = int(input('Qual o tempo em segundos: '))

horas = segundosTotal // 3600
dias = horas // 86400
segRestantes = segundosTotal % 3600
minutos = segRestantes // 60
segFinal = segRestantes % 60


if horas >= 24:
    dias = int(horas/24)
    horas = int(horas % 24)

print(f'{dias} - {horas}:{minutos}:{segFinal}')
