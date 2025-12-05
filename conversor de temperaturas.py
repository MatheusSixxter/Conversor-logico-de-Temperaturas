
print("-=" * 20)
print(" CONVERSOR DE TEMPERATURAS".center(40))
print("-=" * 20)

print("-" * 30)
print(" TABELA DE CONVERSÃO ".center(30))
print("-" * 30)
print("""> Celsius = C
> Fahrenheit = F
> Kelvin = K """)
print("-" * 30)

while True:
    escolha_usuario = "  "
    while escolha_usuario not in "CFK":
        escolha_usuario = str(input(".Escolha sua unidade [C, F, K]: ")).strip().upper()[0]
        if escolha_usuario not in "CFK":
            print("Letra inválida.")

    #Validar usuário:
    if escolha_usuario == "C":
        print("""\n> Você escolheu Celsius!
.Para qual unidade deseja converter ?
------------------
 [F] Fahrenheit
 [K] Kelvin
------------------ """)
        destino = " "
        while destino not in "FK":
            destino = str(input(".Digite a unidade desejada [F/K]: ")).strip().upper()[0]
            if destino not in "FK":
                print(">>> Letra inválida. Tente [F ou K].")

    elif escolha_usuario == "F":
        print("""\n> Você escolheu Fahrenheit!
.Para qual unidade deseja converter ? 
------------------
 [C] Celsius
 [K] Kelvin
------------------ """)
        destino = " "
        while destino not in "CK":
            destino = str(input(".Digite a unidade desejada [C/K]: ")).strip().upper()[0]
            if destino not in "CK":
                print(">>> Letra inválida. Tente [C ou K] ")


    elif escolha_usuario == "K":
        print("""\n> Você escolheu Kelvin!
.Para qual unidade deseja converter ? 
------------------
[C] Celsius
[F] Fahrenheit
------------------ """)
        destino = " "
        while destino not in "CF":
            destino = str(input(".Digite a unidade desejada [C/F]: ")).strip().upper()[0]
            if destino not in "CF":
                print(">>> Letra inválida. Tente [C ou F] ")

    #Bloco Lógico com dicionários:
    unidade_nome = {"C": "°C", "F": "°F", "K": "°K"}
    temp = float(input(f".Qual a temperatura em {unidade_nome[escolha_usuario]} ? "))

    #Fórmulas do programa:
    if escolha_usuario == "C" and destino == "F":
        print("-" * 30)
        print(f"> Resultado de conversão: {(temp * 9/5) + 32:.2f}°F")
        print("-" * 30)

    if escolha_usuario == "C" and destino == "K":
        print("-" * 30)
        print(f"> Resultado de conversão: {temp + 273.15:.2f}°K")
        print("-" * 30)

    if escolha_usuario == "F" and destino == "C":
        print("-" * 30)
        print(f"> Resultado de conversão: {(temp - 32) * 5/9:.2f}°C")
        print("-" * 30)

    if escolha_usuario == "F" and destino == "K":
        print("-" * 30)
        print(f"> Resultado de conversão: {((temp - 32) * 5/9) + 273.15:.2f}°K")
        print("-" * 30)

    if escolha_usuario == "K" and destino == "C":
        print("-" * 30)
        print(f"> Resultado de conversão: {temp - 273.15:.2f}°C")
        print("-" * 30)

    if escolha_usuario == "K" and destino == "F":
        print("-" * 30)
        print(f"> Resultado de conversão: {(temp - 273.15) * 9/5 + 32:.2f}°F")
        print("-" * 30)

    #Se o usuário quer continuar:
    continuar = " "
    while continuar not in "SN":
        continuar =  str(input("> Deseja converter para outra temperatura ? [S/N]: ")).strip().upper()
        if continuar not in "SN":
            print(">> Letra inválida. Escolha entre: S ou N.")
            print("-" * 30)

    if continuar == "N":
        print("-" * 30)
        print(">> Programa encerrado!")
        break






























































