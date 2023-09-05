'''
Crie um algoritmo que seja capaz de descobrir, por meio de perguntas lógicas (verdadeiro ou falso) 
sobre características físicas, um animal que o usuário tenha em mente. Considere os animais: pato, 
águia, galinha, avestruz, pinguim, morcego, ornitorrinco, leão, gato, onça pintada, baleia, tubarão, 
lambari, enguia e arraia.
'''
animais = {
    "pato": ["ave", "tem penas", "voa", "não é carnívoro"],
    "águia": ["ave", "tem penas", "voa", "é carnívoro"],
    "galinha": ["ave", "tem penas", "não voa", "não é carnívoro"],
    "avestruz": ["ave", "tem penas", "não voa", "não é carnívoro"],
    "pinguim": ["ave", "tem penas", "não voa", "não é carnívoro"],
    "morcego": ["mamífero", "tem pelos", "voa", "é carnívoro"],
    "ornitorrinco": ["mamífero", "tem pelos", "não voa", "não é carnívoro"],
    "leão": ["mamífero", "tem pelos", "não voa", "é carnívoro"],
    "gato": ["mamífero", "tem pelos", "não voa", "é carnívoro"],
    "onça pintada": ["mamífero", "tem pelos", "não voa", "é carnívoro"],
    "baleia": ["mamífero", "não tem pelos", "não voa", "não é carnívoro"],
    "tubarão": ["peixe", "não tem pelos", "não voa", "é carnívoro"],
    "lambari": ["peixe", "não tem pelos", "não voa", "não é carnívoro"],
    "enguia": ["peixe", "não tem pelos", "não voa", "não é carnívoro"],
    "arraia": ["peixe", "não tem pelos", "não voa", "não é carnívoro"]
}


def fazer_pergunta(caracteristica):
    resposta = input(f"O animal que você está pensando {caracteristica}? (S para Sim, N para Não): ")
    return resposta.lower() == "s"

animal_adivinhado = None
for animal, caracteristicas in animais.items():
    adivinhou = True
    for caracteristica in caracteristicas:
        if not fazer_pergunta(caracteristica):
            adivinhou = False
            break
    if adivinhou:
        animal_adivinhado = animal
        break


if animal_adivinhado:
    print(f"O animal que você está pensando é um {animal_adivinhado}.")
else:
    print("Não consegui adivinhar o animal que você está pensando.")
