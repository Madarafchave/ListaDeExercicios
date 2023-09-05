'''
Agora altere o algoritmo anterior de maneira que ele verifique os demais níveis de alerta. Considere: 0-
3 é "BAIXO", maior que 3 até 6 "MÉDIO", maior que 6 até 9 "ALTO", para os demais casos é considerado 
"GRAVE". 
'''

# Solicita o nível de alerta ao usuário
nivel_alerta = input("Digite o nível de alerta (de 0 a 10): ")

if nivel_alerta.isdigit() or (nivel_alerta[0] == '-' and nivel_alerta[1:].isdigit()):
    nivel_alerta = int(nivel_alerta)
    
    if 0 <= nivel_alerta <= 10:
        if nivel_alerta <= 3:
            print("Nível de alerta: BAIXO")
        elif nivel_alerta <= 6:
            print("Nível de alerta: MÉDIO")
        elif nivel_alerta <= 9:
            print("Nível de alerta: ALTO")
        else:
            print("Nível de alerta: GRAVE")
    else:
        print("O nível de alerta deve estar entre 0 e 10.")
else:
    print("Por favor, insira um número válido.")

