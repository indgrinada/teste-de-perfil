# PERFIS: A - Líder, B - Pesquisador, C - Executor, D - Revisor

# Início - define as variáveis necessárias
menu = "T"
perfis = {}
    

# Teste - recebe as respostas, computa e apresenta o resultado
def teste(perfis):
    n = 1
    resposta_bruta = "aceito críticas, mas nao fico calada"
    resposta_padrao = []
    opcoes = {"A": 0, "B": 0, "C": 0, "D": 0}

    # Entrada - recebe e padroniza as respostas, até o respondente digitar "F" para finalizar
    print("\nTESTE DE PERFIL COMPORTAMENTAL\n")
    nome = input("Nome do respondente: ").upper()
    print("Digite as respostas dadas, uma em cada linha, ou \"F\" para finalizar:")
    while resposta_bruta != "F":
        resposta_bruta = input(f"{n:2}: ").upper()
        resposta_padrao.append(resposta_bruta)
        n += 1

    # Contagem - conta quantas vezes cada opção (A, B, C, D) aparece nas respostas padronizadas
    for linha in resposta_padrao:
        for char in linha:
            if char in opcoes:
                opcoes[char] += 1

    total = opcoes["A"] + opcoes["B"] + opcoes["C"] + opcoes["D"]
    perfis[nome] = {
        "Líder": opcoes["A"] / total * 100,
        "Pesquisador": opcoes["B"] / total * 100,
        "Executor": opcoes["C"] / total * 100,
        "Revisor": opcoes["D"] / total * 100
    }

    # Saída - exibe o resultado, em porcentagem, para cada face de perfil comportamental
    print("\nRESULTADO DO TESTE\n")
    for face, porcentagem in perfis[nome].items():
        print(f"{face}: {porcentagem:.2f}%")


# Visualização geral - exibe os resultados de todos os respondentes, em porcentagem, para cada face de perfil comportamental
def visual(perfis):
    print("\nRESULTADOS GERAIS")
    for nome in perfis.keys():
        print(f"\n{nome}: ")
        for face, porcentagem in perfis[nome].items():
            print(f"{face}: {porcentagem:.2f}%")


# Menu - permite, ao respondente, escolher entre realizar outro teste, visualizar os resultados ou sair do programa
while menu != "S":
    if menu == "T":
        teste(perfis)
        menu = input("\n\nDigite \"T\" para realizar outro teste, \"V\" para visualizar os resultados, ou \"S\" para sair do programa: ").upper()
    elif menu == "V":
        visual(perfis)
        menu = input("\n\nDigite \"T\" para realizar outro teste, \"V\" para visualizar os resultados, ou \"S\" para sair do programa: ").upper()
    else:
        menu = input("Opção inválida. Digite \"T\" para realizar outro teste, \"V\" para visualizar os resultados, ou \"S\" para sair do programa: ").upper()

print("\n\nFim do programa.")