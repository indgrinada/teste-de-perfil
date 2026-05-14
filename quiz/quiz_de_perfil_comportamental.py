import customtkinter as ctk
import json

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TESTE DE PERFIL")
        self.geometry("600x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame com Scroll
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Teste de Perfil Comportamental")
        self.scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Campo Nome
        self.nome_lbl = ctk.CTkLabel(self.scroll_frame, text="Nome do respondente:")
        self.nome_lbl.grid(row=0, column=0, padx=10, pady=4, sticky="w")
        self.nome_ent = ctk.CTkEntry(self.scroll_frame)
        self.nome_ent.grid(row=1, column=0, padx=10, pady=4, sticky="ew")

        # Carga do JSON
        with open("avaliação_de_perfil.json", "r", encoding="utf-8") as a:
            self.lista_perguntas = json.load(a)

        self.lista_respostas = []
        
        # Controle de linhas internas do scroll_frame (começa em 2 pois 0 e 1 são o nome)
        linha_atual = 2 

        # Loop de criação das perguntas
        for i, pergunta in enumerate(self.lista_perguntas):
            linha_atual = self.criar_pergunta(i, pergunta, linha_atual)

        # Botão de cálculo
        self.calcular_btn = ctk.CTkButton(self, text="Calcular Resultado", command=self.calcular_resultado)
        self.calcular_btn.grid(row=1, column=0, pady=20)

        self.resultado_txt = ctk.CTkTextbox(self, height=120, activate_scrollbars=True)
        self.resultado_txt.grid(row=2, column=0, padx=10, pady=(0, 15), sticky="ew")

    def criar_pergunta(self, i, pergunta, linha):
        pergunta_lbl = ctk.CTkLabel(self.scroll_frame, text=pergunta["pergunta"])
        pergunta_lbl.grid(row=linha, column=0, padx=10, pady=(10), sticky="w")
        linha += 1

        resposta = ctk.StringVar(value="None") 
        self.lista_respostas.append(resposta)

        for i, opcao in enumerate(pergunta["opcoes"]):
            opcao_rbtn = ctk.CTkRadioButton(self.scroll_frame, text=opcao, variable=resposta, value=str(i))
            opcao_rbtn.grid(row=linha, column=0, padx=20, pady=2, sticky="w")
            linha += 1 
        return linha

    def calcular_resultado(self):
        perfis = {"Lider": 0, "Pesquisador": 0, "Pratico": 0, "Analista": 0}
        
        for i, resposta in enumerate(self.lista_respostas):
            valor_resposta = resposta.get()
            if valor_resposta != "None":
                indice = int(valor_resposta)
                perfil_escolhido = self.lista_perguntas[i]["perfis"][indice]
                perfis[perfil_escolhido] += 1
        
        nome = self.nome_ent.get()
        dominante = max(perfis, key=perfis.get)
        
        # Validação caso o usuário não digite o nome
        if not nome.strip():
            nome = "Usuário Anônimo"

        self.resultado_txt.delete("0.0", "end")
        self.resultado_txt.insert("0.0", (f"O perfil dominante de {nome} é: {dominante}"))

if __name__ == "__main__":
    app = App()
    app.mainloop()
