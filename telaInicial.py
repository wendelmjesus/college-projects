import tkinter as tk
from OrientacaoCarreira import abrir_orientacao_de_carreira  #Importando a próxima tela.

def acao_botao():
    janela.destroy()  
    abrir_orientacao_de_carreira() #Chama a próxima tela.

janela = tk.Tk()
janela.title("Tela Inicial")
janela.geometry("500x500") #Resolução da Janela.

#Texto
mensagemBemVindo = tk.Label(janela, text="Olá, Seja bem-vindo!", font=("Arial", 12, "bold","italic"), fg= "#946CE6")
mensagemBemVindo.pack(pady=160)

#Texto
textoInicio = tk.Label(janela, text="Vamos começar o Teste de", font=("Arial", 16))
textoInicio.place(relx=0.5, rely=0.40, anchor="center")

#Texto
textoOrientacaoVocacional = tk.Label(janela, text="Orientação Vocacional?", font=("Arial", 16, "bold"), fg="#946CE6")
textoOrientacaoVocacional.place(relx=0.5, rely=0.45, anchor="center")

#Criação do botão para iniciar o teste.
def criar_botao_iniciar(texto, comando):
    return tk.Button(janela, text=texto, font=("Arial", 12, "bold"), width=10, height=1, 
                     bg="#946CE6", fg="white", activebackground="#7a4ec9", activeforeground="white", 
                     relief="flat", bd=0, command=comando)

botaoIniciar = criar_botao_iniciar("Iniciar", acao_botao)
botaoIniciar.place(relx=0.5, rely=0.53, anchor="center")

janela.mainloop()
