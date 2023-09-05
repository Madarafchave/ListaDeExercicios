'''
Escreva um algoritmo para cadastro de dados básicos de alunos. O usuário deve informar o número da 
matrícula (cinco dígitos), nome completo do aluno, gênero (o usuário deve informar “M” ou “F”), curso 
(o usuário deve informar “BES”, “BEC” ou “ADS”) e coeficiente de rendimento (dever ser maior ou igual 
a zero e menor ou igual a 100). Como resultado o sistema deve imprimir a matrícula, o nome do aluno, 
gênero (deve imprimir “Masculino” ou “Feminino”), curso (“Bacharelado em Engenharia de Software” 
para “BES”, “Bacharelado em Engenharia de Computação” para “BEC” e “Analise e Desenvolvimento 
de Sistemas” para “ADS”), o coeficiente de rendimento, seguido por “Excelente” se o coeficiente for [90, 
100], “Bom” se entre [70, 90), “Regular” se entre [50, 70), “Necessita melhoras” se entre [30, 50) e 
“Preocupante” se entre [0, 30). Note a existência de intervalos fechados e semifechados para os 
coeficientes.
'''
def obter_curso(sigla):
    cursos = {"BES": "Bacharelado em Engenharia de Software",
              "BEC": "Bacharelado em Engenharia de Computação",
              "ADS": "Análise e Desenvolvimento de Sistemas"}
    return cursos.get(sigla, "Curso Desconhecido")


matricula = input("Informe o número da matrícula (cinco dígitos): ")
nome = input("Informe o nome completo do aluno: ")
genero = input("Informe o gênero (M para Masculino ou F para Feminino): ")
curso_sigla = input("Informe a sigla do curso (BES, BEC ou ADS): ")
coeficiente = float(input("Informe o coeficiente de rendimento (de 0 a 100): "))


genero_completo = "Masculino" if genero == "M" else "Feminino"


if 90 <= coeficiente <= 100:
    classificacao = "Excelente"
elif 70 <= coeficiente < 90:
    classificacao = "Bom"
elif 50 <= coeficiente < 70:
    classificacao = "Regular"
elif 30 <= coeficiente < 50:
    classificacao = "Necessita melhoras"
elif 0 <= coeficiente < 30:
    classificacao = "Preocupante"
else:
    classificacao = "Coeficiente fora do intervalo válido"


print("\nDados do Aluno:")
print("Matrícula:", matricula)
print("Nome:", nome)
print("Gênero:", genero_completo)
print("Curso:", obter_curso(curso_sigla))
print("Coeficiente de Rendimento:", coeficiente)
print("Classificação:", classificacao)
