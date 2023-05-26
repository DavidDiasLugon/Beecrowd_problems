# Ler o número do funcionário
num_funcionario = int(input())
# Ler o número de horas trabalhadas
hrs_trab = int(input())
# Valor por hora
valor_por_horas = float(input())
# Calcular o salário
salario = (valor_por_horas * hrs_trab)


print(f'NUMBER = {num_funcionario}\nSALARY = U$ {salario:.2f}')
