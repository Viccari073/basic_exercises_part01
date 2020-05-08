"""
Faça um porgrama para converter uma letra maiúscula em letra minuscula.
Use a tabela ASCII para resolver o problema.
"""

minus = input('Digite uma letra minúscula:')
print(f'A letra {minus} em maiúsculo fica: {chr(ord(minus)-32)}')

# chr - converte a letra para o número (posição na tabela ASCII)
# ord - converte o número (posição da tabela ASCII) para a letra correspondente)
# -32 - corresponde a distância entre a letra minúscula e maúscula na tabela ASCII
