"""
PERFIS
A - Líder
B - Pesquisador
C - Executor 
D - Revisor 

"""
resposta_bruta = "aceito críticas, mas nao fico calada"
resposta_padrao = []
opcoes = {"A": 0, "B": 0, "C": 0, "D": 0}

print("TESTE DE PERFIL COMPORTAMENTAL")
print("Responda as perguntas com as opções A, B, C ou D. Digite uma resposta por linha, ou o digito 'F' para finalizar:")
while resposta_bruta != "F":
     resposta_bruta = input().upper()
     resposta_padrao.append(resposta_bruta)

# Contagem 
for linha in resposta_padrao:
   for char in linha:
       if char in opcoes:
           opcoes[char] += 1

n = opcoes["A"] + opcoes["B"] + opcoes["C"] + opcoes["D"]

# Saída
print("RESULTADO DO TESTE:")
for perfil, percil in opcoes.items():
    print(f"{perfil}: {(percil/n)*100:.2f}%")
    print(opcoes["A"])