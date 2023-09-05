'''
Lista de exercicios

3- Crie um algoritmo que, dado três números 
informados pelo usuário, informe qual é o menor deles
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
menor_numero = n1
if n2 < menor_numero:
    maior_numero = n2
if n3 < menor_numero:
    menor_numero = n3
print(f"O menor número é {menor_numero}")
