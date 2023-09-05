'''
Agora altere o algoritmo anterior de maneira que ele permita que o professor, antes de informar as notas, 
informe os seus respectivos pesos. Depois disso o algoritmo deve, de análoga ao exercício anterior, 
calcular a média, no entanto, agora considerando os seus pesos. Lembrete: A soma dos pesos das 
notas sempre deve ser 10.
'''
nota1 = float(input("Informe a nota 1: "))
peso1 = float(input("Informe o peso da nota 1 (deve ser um valor entre 0 e 10): "))
nota2 = float(input("Informe a nota 2: "))
peso2 = float(input("Informe o peso da nota 2 (deve ser um valor entre 0 e 10): "))
nota3 = float(input("Informe a nota 3: "))
peso3 = float(input("Informe o peso da nota 3 (deve ser um valor entre 0 e 10): "))

soma_pesos = peso1 + peso2 + peso3
if soma_pesos != 10:
    print("A soma dos pesos das notas deve ser igual a 10. Por favor, verifique os pesos informados.")
else:
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / 10
    print(f"A média ponderada das notas é: {media_ponderada:.2f}")
