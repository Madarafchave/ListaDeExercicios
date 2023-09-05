
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
if n1 < n2:
    numero1, n2 = n2, n1

if n2 < n3:
    n2, n3 = n3, n2

if n1 < n2:
    n1, n2 = n2, n1
print("Os números em ordem decrescente são:", n1, n2, n3)
