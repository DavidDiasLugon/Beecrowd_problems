p1 = input()  # Insere a linha com os valores da peça 1
valores_p1 = p1.split()  # Divide a linha em 3 itens
p2 = input()  # Insere a linha com os valores da peça 2
valores_p2 = p2.split()  # Divide a linha em 3 itens

total_pagar = (int(valores_p1[1]) * float(valores_p1[2])) + \
    (int(valores_p2[1]) * float(valores_p2[2]))
print(f'VALOR A PAGAR: R$ {total_pagar:.2f}')
