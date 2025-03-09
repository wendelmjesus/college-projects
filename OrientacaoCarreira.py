import tkinter as tk
import random
from resultados import exibir_resultados  

#Cria a janela de Orientação Vocacional
def abrir_orientacao_de_carreira():
    janela_orientacao = tk.Tk()
    janela_orientacao.title("Orientação Vocacional")
    janela_orientacao.geometry("600x500")  
    janela_orientacao.config(bg="#F0F4F7")

    #Lista de Perguntas da Orientação Vocacional.
    perguntas = [
        ("Você gosta de resolver problemas lógicos?", ["Tecnologia e Inovação"]),
        ("Você se interessa por criar e desenvolver tecnologias?", ["Tecnologia e Inovação"]),
        ("Você gosta de expressar sua criatividade em projetos artísticos?", ["Artes e Criatividade"]),
        ("Você se sente motivado a ajudar pessoas com suas habilidades?", ["Saúde e Bem-Estar"]),
        ("Você gosta de estudar o comportamento humano?", ["Ciências Sociais"]),
        ("Você tem interesse em ensinar ou compartilhar conhecimentos?", ["Educação"]),
        ("Você se preocupa com o meio ambiente e sustentabilidade?", ["Meio Ambiente"]),
        ("Você gosta de lidar com números e cálculos financeiros?", ["Finanças"]),
    ]
    
    #Embaralha a ordem das perguntas
    random.shuffle(perguntas)
    
    respostas = []  # Lista para armazenar respostas do usuário.
    pergunta_atual = 0  # Indica qual pergunta será exibida.

    #Função que processa a resposta e avança para a próxima pergunta.
    def obter_resposta(resposta):
        nonlocal pergunta_atual
        respostas.append(resposta)

        pergunta_atual += 1
        if pergunta_atual < len(perguntas):
            label_pergunta.config(text=perguntas[pergunta_atual][0])
            label_contagem.config(text=f"Pergunta {pergunta_atual + 1} de {len(perguntas)}")  
            if pergunta_atual == 1:
                button_voltar.place(x=250, y=350)  
        else:
            exibir_resultados(janela_orientacao, respostas)  

    #Função para voltar a pergunta anterior.
    def voltar_resposta():
        nonlocal pergunta_atual
        if pergunta_atual > 0:
            pergunta_atual -= 1
            respostas.pop()  
            label_pergunta.config(text=perguntas[pergunta_atual][0])
            label_contagem.config(text=f"Pergunta {pergunta_atual + 1} de {len(perguntas)}")  
            if pergunta_atual == 0:
                button_voltar.place_forget()  

    frame_perguntas = tk.Frame(janela_orientacao, bg="#F0F4F7")
    frame_perguntas.pack(expand=True)

    fonte_pergunta = ("Arial", 14, "bold")
    fonte_botao = ("Arial", 12)

    label_pergunta = tk.Label(frame_perguntas, text=perguntas[0][0], font=fonte_pergunta, bg="#F0F4F7", wraplength=500)
    label_pergunta.pack(pady=10)

    #Exibe a contagem das perguntas.
    label_contagem = tk.Label(janela_orientacao, text=f"Pergunta 1 de {len(perguntas)}", font=("Arial", 10), bg="#F0F4F7")
    label_contagem.place(x=250, y=150)

    botao_frame = tk.Frame(frame_perguntas, bg="#F0F4F7")
    botao_frame.pack(pady=5)

    #Função dos botões SIM ou NÃO.
    def criar_botao_resposta(texto, resposta, cor_bg):
        return tk.Button(botao_frame, text=texto, font=fonte_botao, width=15, height=2, 
                         bg=cor_bg, fg="white", activebackground="#7a4ec9", activeforeground="white", 
                         relief="flat", bd=0, command=lambda: obter_resposta(resposta))
    
    button_sim = criar_botao_resposta("Sim", True, "#946CE6")
    button_sim.pack(side="left", padx=5)

    button_nao = criar_botao_resposta("Não", False, "#788EF0")
    button_nao.pack(side="right", padx=5)

    #Botão para voltar a pergunta anterior.
    button_voltar = tk.Button(janela_orientacao, text="Voltar", font=fonte_botao, width=10, height=1, 
                              bg="#C5BFBF", fg="white", activebackground="#FFC000", activeforeground="white", 
                              relief="flat", bd=0, command=voltar_resposta)
    button_voltar.place_forget()

    janela_orientacao.mainloop()
