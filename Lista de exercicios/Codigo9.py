'''
Crie um algoritmo que, dados os lados de um triângulo informados pelo usuário, calcule a área.
'''
import math

lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))

semiperimetro = (lado1 + lado2 + lado3) / 2

area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))

if area > 0:
    print(f"A área do triângulo é {area:.2f} unidades quadradas.")
else:
    print("Não é possível formar um triângulo com esses lados.")
