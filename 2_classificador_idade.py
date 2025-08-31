# Atividade Prática 03 - Questão 2
#
# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:
# Criança (0-12 anos),
# Adolescente (13-17 anos),
# Adulto (18-59 anos)
# Idoso (60 anos ou mais).
#
# -----------------------------------------------------------------

# Exemplo resolvido:
idade = 15
if 0 <= idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print("Exemplo resolvido:")
print(f"A pessoa com {idade} anos é classificada como: {classificacao}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
idade_nova = int(input("Digite a idade: "))

if 0 <= idade_nova <= 12:
    classificacao_nova = "Criança"
elif 13 <= idade_nova <= 17:
    classificacao_nova = "Adolescente"
elif 18 <= idade_nova <= 59:
    classificacao_nova = "Adulto"
else:
    classificacao_nova = "Idoso"

print(f"A pessoa com {idade_nova} anos é classificada como: {classificacao_nova}")
