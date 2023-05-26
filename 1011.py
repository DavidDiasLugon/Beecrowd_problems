pi = 3.14159  # Definindo uma aproximação para o valor de pi
raio = int(input())  # Inserido o valor do raio

# Cálculo do volume de esferas (4/3) * pi * r^3
volume_esfera = (4/3) * pi * pow(raio, 3)

print(f'VOLUME = {volume_esfera:.3f}')
