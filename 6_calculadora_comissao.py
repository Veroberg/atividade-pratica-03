# Atividade Prática 03 - Questão 6
#
# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
# efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
# sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
nome = "Joao"
salario_fixo = 1500.00
vendas = 1230.30

comissao = vendas * 0.15
total_a_receber = salario_fixo + comissao

print("Exemplo resolvido:")
print(f"TOTAL = R$ {total_a_receber:.2f}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
nome_novo = input("Digite o nome do vendedor: ")
salario_fixo_novo = float(input("Digite o salário fixo: "))
vendas_novas = float(input("Digite o total de vendas: "))

comissao_nova = vendas_novas * 0.15
total_a_receber_novo = salario_fixo_novo + comissao_nova

print(f"TOTAL = R$ {total_a_receber_novo:.2f}")
