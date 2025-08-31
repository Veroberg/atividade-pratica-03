# Atividade Prática 03 - Questão 3
#
# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.
# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"
#
# -----------------------------------------------------------------

# Exemplo resolvido:
peso = 70.0
altura = 1.75
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("Exemplo resolvido:")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
peso_novo = float(input("Digite o peso (em kg): "))
altura_nova = float(input("Digite a altura (em metros): "))
imc_novo = peso_novo / (altura_nova ** 2)

if imc_novo < 18.5:
    classificacao_nova = "Abaixo do peso"
elif imc_novo < 25:
    classificacao_nova = "Peso normal"
elif imc_novo < 30:
    classificacao_nova = "Sobrepeso"
else:
    classificacao_nova = "Obeso"

print(f"IMC: {imc_novo:.2f}")
print(f"Classificação: {classificacao_nova}")
