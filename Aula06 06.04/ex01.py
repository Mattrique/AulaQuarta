freq=float(input("Digite sua frequencia"))
m=float(input("Digite sua media"))

if freq<75:
    print("Reprovado por falta")
elif m <6:
    print("Reprovado por nota")
else:
    print("Aprovado!")

