# Ler dois valores de ponto flutuante (A e B)
nota_1 = float(input())
nota_2 = float(input())

# Calcular a média das duas notas(dividindo pela soma dos pesos), com peso 3.5 na primeira e peso 7.5 na segunda
media = ((nota_1 * 3.5) + (nota_2 * 7.5))/11

# Imprimir a média com 5 casas decimais
print('MEDIA =', f'{media:1.5f}')
