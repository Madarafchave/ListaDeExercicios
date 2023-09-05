'''
Problemas simples do cotidiano podem representar desafios para o mundo computacional. Faça um 
algoritmo que, dados três números inteiros representando dia, mês e ano de uma data, imprima qual o 
dia seguinte. 
'''

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))


dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if eh_bissexto(ano):
    dias_por_mes[2] = 29

if 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes]:
    # Incrementa o dia
    dia += 1
    if dia > dias_por_mes[mes]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1

    print(f"O dia seguinte é: {dia:02d}/{mes:02d}/{ano}")
else:
    print("Data inválida.")
