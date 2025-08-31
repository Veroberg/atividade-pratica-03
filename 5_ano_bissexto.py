# Atividade Prática 03 - Questão 5
#
# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
ano = 2024
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"Exemplo resolvido:")
    print(f"O ano {ano} é bissexto.")
else:
    print(f"Exemplo resolvido:")
    print(f"O ano {ano} não é bissexto.")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
ano_novo = int(input("Digite um ano: "))
if (ano_novo % 4 == 0 and ano_novo % 100 != 0) or (ano_novo % 400 == 0):
    print(f"O ano {ano_novo} é bissexto.")
else:
    print(f"O ano {ano_novo} não é bissexto.")
