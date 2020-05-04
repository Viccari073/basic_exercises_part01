"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora).
A fórmula de conversão é k = m * 3.6, sendo k a velocidade em km/h e m em m/s.
"""

metros_por_segundo = float(input('Qual a velocidade em m/s?'))
km_por_hora = metros_por_segundo * 3.6
print(f'A velocidade de {metros_por_segundo}m/s corresponde à{km_por_hora: .2f}km/h')