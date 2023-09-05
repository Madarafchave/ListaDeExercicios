'''
Considerando o sistema de notas da UniEVANGÉLICA, construa um algoritmo que, dadas 4 notas 
parciais de um aluno pelo usuário, calcule a média e imprima se o aluno foi aprovado ou reprovado. 
Considere os 3 ciclos
'''

nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))
nota3 = float(input("Digite a terceira nota parcial: "))
nota4 = float(input("Digite a quarta nota parcial: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7.0:
    print(f"A média do aluno é {media:.2f}, e ele foi aprovado.")
elif media >= 4.0:
    print(f"A média do aluno é {media:.2f}, e ele está em recuperação.")
else:
    print(f"A média do aluno é {media:.2f}, e ele foi reprovado.")
