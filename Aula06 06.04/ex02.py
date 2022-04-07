tipo = input("Digite qual tipo de diaria: \nS - Simples \nD - Duplo \nT - Triplo:")
qtdeDiarias = int(input("Digite a quantidade de diarias:"))

if tipo == 's' or tipo == 'S':
    print("Valor a pagar : ",(qtdeDiarias * 255.5))
elif tipo == 'd' or tipo == 'D':
    print("Valor a pagar : ",(qtdeDiarias * 305.5))
elif tipo == 't' or tipo == 'T':
    print("Valor a pagar : ",(qtdeDiarias * 360.5))
else:
    print("Tipo de hospedagem invalida")


