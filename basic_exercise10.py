"""
Leia uma velocidad em km/h (quilômetros por hora) e apresnete-a convertida em m/s (metros por segundo).
A fórmula de conversão é: m = k/3.6, sendo k a velocidade em km/h e m em m/s.

"""

km_por_hora = float(input('Qual a velocidade em km/h?'))
m_por_seg = km_por_hora / 3.6
print(f'A velocidade de {km_por_hora}km/h corresponde à {m_por_seg: .2f}m/s.')

