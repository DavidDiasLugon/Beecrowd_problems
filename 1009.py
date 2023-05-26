vendedor = input()  # Informa o nome do vendedor
salario_fixo = float(input())  # Informa o salário fixo do vendedor
# Informa o dinheiro arrecadado com as vendas no mês
valor_vendas = float(input())

# Adiciona ao salário fixo 15%(comissão) do valor das vendas no mês
salario_final = salario_fixo + ((15/100)*valor_vendas)

print(f'TOTAL = R$ {salario_final:.2f}')
