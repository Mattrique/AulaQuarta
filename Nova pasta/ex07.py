contador = 0

soma = 0
resp = 's'

while resp == 's' or resp =='S':
    num = float(input("Digite um numero: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja digitar um novo numero : (S/N)")
    media =soma/contador
    print("A media dos numeros é: ",media)