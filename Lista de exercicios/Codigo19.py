'''
Faça um algoritmo que, dado o valor total em reais e o número de prestações desejadas, calcule o valor 
de cada prestação. O número mínimo de prestações deve ser 12. Se o número de prestações for maior 
ou igual a 24, adicione 10% de juros ao valor total, se for maior ou igual a 36, adicione 15% de juros ao 
valor total
'''
valor_total = float(input("Digite o valor total em reais: "))
num_prestacoes = int(input("Digite o número de prestações (mínimo de 12): "))
if num_prestacoes < 12:
    print("O número mínimo de prestações deve ser 12.")
else:
    valor_prestacao = valor_total / num_prestacoes

    if num_prestacoes >= 36:
        valor_prestacao *= 1.15  # Adiciona 15% de juros
    elif num_prestacoes >= 24:
        valor_prestacao *= 1.10  # Adiciona 10% de juros
    print(f"O valor de cada prestação é de R${valor_prestacao:.2f}")
