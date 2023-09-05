'''
Lista de exercicios

2- Crie um algoritmo que, dado três números
informados pelo usuário, informe qual é o maior deles.
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
maior_numero = n1
if n2 > maior_numero:
    maior_numero = n2
if n3 > maior_numero:
    maior_numero = n3
print(f"O maior número é {maior_numero}")

