# Nota A (Peso 2)
# Nota B (Peso 3)
# Nota C (Peso 5)

nota_A = float(input())
nota_B = float(input())
nota_C = float(input())

# 10 é a soma de todos os pesos, pois é uma média ponderada
media_ponderada = ((nota_A * 2) + (nota_B * 3) + (nota_C * 5))/(10)

# Imprimir com a formatação adequada, 1 dígito após a casa decimal
print(f'MEDIA = {media_ponderada:.1f}')
