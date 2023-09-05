'''
Lista de exercicios

4- Crie um algoritmo que, dado o nível de alerta de risco, 
imprima se ele for GRAVE. O nível de alerta é um número que 
varia de 0 a 10. O nível é considerado GRAVE quando ele é superior a 9.
'''

nivel_alerta = input("Digite o nível de alerta (de 0 a 10): ")


if nivel_alerta.isdigit():
    nivel_alerta = int(nivel_alerta)
    if nivel_alerta > 9:
        print("Nível de alerta GRAVE!")
    else:
        print("Nível de alerta não é GRAVE.")
else:
    print("Por favor, insira um número válido entre 0 e 10.")
