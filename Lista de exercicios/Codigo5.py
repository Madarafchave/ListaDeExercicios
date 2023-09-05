'''
Agora altere o algoritmo anterior de maneira que ele verifique também se o nível informado está entre 0 
e 10. Caso contrário uma mensagem de erro deve ser apresenta.
nivel_alerta = input("Digite o nível de alerta (de 0 a 10): ")
'''

nivel_alerta = input("Digite o nível de alerta (de 0 a 10): ")
if nivel_alerta.isdigit() or (nivel_alerta[0] == '-' and nivel_alerta[1:].isdigit()):
    nivel_alerta = int(nivel_alerta)
    
    if 0 <= nivel_alerta <= 10:
        if nivel_alerta > 9:
            print("Nível de alerta GRAVE!")
        else:
            print("Nível de alerta não é GRAVE.")
    else:
        print("O nível de alerta deve estar entre 0 e 10.")
else:
    print("Por favor, insira um número válido.")


