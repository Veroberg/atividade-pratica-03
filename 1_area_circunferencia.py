# Atividade Prática 03 - Questão 1
#
# A fórmula para calcular a área de uma circunferência é: área = π ×raio². Considerando para
# este problema que π = 3.14159265:
# Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
# Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável
# raio.
# Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
# abaixo, com 4 casas após o ponto decimal.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
import math

raio = 5.0
pi = 3.14159265
area = pi * (raio ** 2)

print("Exemplo resolvido:")
print(f"A={area:.4f}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
raio_novo = float(input("Digite o valor do raio: "))
area_nova = pi * (raio_novo ** 2)
print(f"A={area_nova:.4f}")
