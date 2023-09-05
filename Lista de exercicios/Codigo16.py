'''
Você viajou para os Estados Unidos e descobriu que lá a unidade de medida de temperatura é diferente 
da do Brasil. Para não ter que acessar um serviço na internet a todo o momento, nem fazer os cálculos 
manualmente, faça um algoritmo que converte a temperatura, dada uma unidade de medida e uma 
temperatura. Ou seja, se a data for informada em Celsius o algoritmo deve fornecer a temperatura em 
Fahrenheit, já se a temperatura for fornecida em Fahrenheit, o resultado deve ser em graus Celsius. 
'''
def celsius_para_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

def fahrenheit_para_celsius(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    return temp_celsius
print("Selecione a unidade de medida:")
print("1. Celsius")
print("2. Fahrenheit")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    temp_celsius = float(input("Informe a temperatura em graus Celsius: "))
    temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
    print(f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f} °F")
elif opcao == 2:
    temp_fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
    temp_celsius = fahrenheit_para_celsius(temp_fahrenheit)
    print(f"A temperatura em Celsius é: {temp_celsius:.2f} °C")
else:
    print("Opção inválida. Por favor, escolha 1 para Celsius ou 2 para Fahrenheit.")
