# Atividade Prática 03 - Questão 4
#
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
#
# -----------------------------------------------------------------

# Código interativo:
def converter_temperatura(temp, unidade_origem, unidade_destino):
    if unidade_origem.upper() == "C":
        if unidade_destino.upper() == "F":
            return (temp * 9/5) + 32
        elif unidade_destino.upper() == "K":
            return temp + 273.15
        else:
            return temp
    elif unidade_origem.upper() == "F":
        if unidade_destino.upper() == "C":
            return (temp - 32) * 5/9
        elif unidade_destino.upper() == "K":
            return (temp - 32) * 5/9 + 273.15
        else:
            return temp
    elif unidade_origem.upper() == "K":
        if unidade_destino.upper() == "C":
            return temp - 273.15
        elif unidade_destino.upper() == "F":
            return (temp - 273.15) * 9/5 + 32
        else:
            return temp

print("Conversor de Temperatura (C, F, K)")
temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ")
unidade_destino = input("Digite a unidade de destino (C, F ou K): ")

temperatura_convertida = converter_temperatura(temperatura, unidade_origem, unidade_destino)
print(f"{temperatura} {unidade_origem.upper()} equivalem a {temperatura_convertida:.2f} {unidade_destino.upper()}")
