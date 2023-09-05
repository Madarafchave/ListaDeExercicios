'''
Crie um algoritmo que, dado três números informados pelo usuário, verifique se algum deles é múltiplo 
de outro. Note que pode haver mais de um múltiplo entre eles. 
'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if (n1 % n2 == 0) or (n1 % n3 == 0):
    print(f"{n1} é múltiplo de {n2} ou {n3}.")

if (n2 % n1 == 0) or (n2 % n3 == 0):
    print(f"{n2} é múltiplo de {n1} ou {n3}.")

if (n3 % n1 == 0) or (n3 % n2 == 0):
    print(f"{n3} é múltiplo de {n1} ou {n2}.")
