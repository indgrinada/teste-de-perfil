# PERFIS: A - Líder, B - Pesquisador, C - Executor, D - Revisor

# Início - define as variáveis necessárias
menu = "T"
perfis = {}
mensagem = """

Digite:

T para realizar outro teste
V para visualizar os resultados
S para salvar o relatório
E para excluir registros
F para finalizar \n\n"""
    

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
    if total == 0: total = 1  # Evita divisão por zero

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


# Salvamento - gera um txt dos resultados gerais
def salva(perfis):
    with open("relatorio_perfis.txt", "w") as arquivo:
        arquivo.write(f"RESULTADOS GERAIS\n")
        for nome in perfis.keys():
            arquivo.write(f"\n{nome}:\n")
            for face, porcentagem in perfis[nome].items():
                arquivo.write(f"{face}: {porcentagem:.2f}%\n")
    print("\nRelatório salvo como \"relatorio_perfis.txt\"!")


# Exclusão - exclui o registro do respondente indicado, caso necessário
def exclui(perfis):
    nome = input("Digite o nome do respondente a ser excluído: ").upper()
    if nome in perfis:
        del perfis[nome]
        print(f"\nRegistro de {nome} excluído com sucesso!")
    else:
        print(f"\nRegistro de {nome} não encontrado.")


# Menu - permite, ao respondente, escolher entre realizar outro teste, visualizar os resultados ou sair do programa
while menu != "F":
    if menu == "T":
        teste(perfis)
        menu = input(f"{mensagem}T/V/S/E/F: ").upper()
    elif menu == "V":
        visual(perfis)
        menu = input(f"{mensagem}T/V/S/E/F: ").upper()
    elif menu == "S":
        salva(perfis)
        menu = input(f"{mensagem}T/V/S/E/F: ").upper()
    elif menu == "E":
        exclui(perfis)
        menu = input(f"{mensagem}T/V/S/E/F: ").upper()
    else:
        menu = input(f"Opção inválida. \n{mensagem}T/V/S/E/F: ").upper()

print("\n\nFim do programa.")
