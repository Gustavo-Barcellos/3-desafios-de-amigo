def executar_turno(atacante, defensor):
    # Verifica se pode usar especial
    if atacante["cooldown"] == 0:
        dano = atacante["especial"] - defensor["defesa"]
        dano = max(1, dano)
        defensor["vida"] -= dano
        atacante["cooldown"] = 2  # ativa cooldown
        print(f"{atacante['nome']} usou ATAQUE ESPECIAL e causou {dano} de dano!")
    else:
        dano = atacante["ataque"] - defensor["defesa"]
        dano = max(1, dano)
        defensor["vida"] -= dano
        atacante["cooldown"] -= 1
        print(f"{atacante['nome']} usou ataque normal e causou {dano} de dano.")

    # Mostra status de vida após o ataque
    print(f"{defensor['nome']} agora tem {defensor['vida']} de vida.\n")

def simular_batalha(kratos, baldur):
    turno = 0
    print("A batalha começou!\n")
    while kratos["vida"] > 0 and baldur["vida"] > 0:
        if turno % 2 == 0:
            executar_turno(kratos, baldur)
        else:
            executar_turno(baldur, kratos)
        turno += 1

    # Resultado final
    if kratos["vida"] <= 0 and baldur["vida"] <= 0:
        print("Empate! Ambos morreram.")
    elif kratos["vida"] <= 0:
        print("Baldur venceu!")
    else:
        print("Kratos venceu!")

# Dados dos personagens
kratos = {
    "nome": "Kratos",
    "vida": 100,
    "ataque": 20,
    "especial": 40,
    "defesa": 5,
    "cooldown": 0
}

baldur = {
    "nome": "Baldur",
    "vida": 100,
    "ataque": 18,
    "especial": 35,
    "defesa": 6,
    "cooldown": 0
}

# Executar batalha
simular_batalha(kratos, baldur)