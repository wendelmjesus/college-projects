import tkinter as tk

def exibir_resultados(janela_orientacao, respostas):
    janela_orientacao.destroy()

    contagem_areas = {
        "Tecnologia e Inovação": 0,
        "Artes e Criatividade": 0,
        "Saúde e Bem-Estar": 0,
        "Ciências Sociais": 0,
        "Educação": 0,
        "Meio Ambiente": 0,
        "Finanças": 0,
    }

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

    #Atualiza as contagens para cada área com base nas respostas
    for i, resposta in enumerate(respostas):
        if resposta:  # Se a resposta for verdadeira (sim), incrementa a contagem da área
            for area in perguntas[i][1]:
                contagem_areas[area] += 1

    # Seleciona a área com maior pontuação
    area_interesse = max(contagem_areas, key=contagem_areas.get)

    #Descrição 
    descricao = {
        "Tecnologia e Inovação": "Áreas que envolvem desenvolvimento de software, inovação tecnológica e automação.",
        "Artes e Criatividade": "Carreiras voltadas para expressão criativa, como design, música ou artes visuais.",
        "Saúde e Bem-Estar": "Profissões que envolvem cuidar da saúde física e mental das pessoas.",
        "Ciências Sociais": "Áreas voltadas para o entendimento de dinâmicas culturais, históricas e sociais.",
        "Educação": "Trabalhar com ensino e desenvolvimento de métodos educacionais.",
        "Meio Ambiente": "Profissões voltadas para sustentabilidade e preservação ambiental.",
        "Finanças": "Carreiras relacionadas à economia, investimentos e análise de dados financeiros.",
    }

    janela_resultados = tk.Tk()
    janela_resultados.title("Resultados da Orientação Vocacional")
    janela_resultados.geometry("460x350")
    janela_resultados.config(bg="#F0F4F7")

    frame_resultados = tk.Frame(janela_resultados, bg="#F0F4F7", padx=15, pady=10)
    frame_resultados.pack(fill="both", expand=True)

    label_titulo = tk.Label(frame_resultados, text="Resultado:", font=("Arial", 18, "bold"), bg="#F0F4F7", fg="#FFC000")
    label_titulo.pack(pady=10)

    label_area = tk.Label(frame_resultados, text=area_interesse, font=("Arial", 16, "bold"), bg="#F0F4F7", fg="#2E3B4E")
    label_area.pack(pady=5)

    label_descricao = tk.Label(frame_resultados, text=descricao[area_interesse], font=("Arial", 12), bg="#F0F4F7", fg="#2E3B4E", wraplength=350)
    label_descricao.pack(pady=10)

    #Função do botão fechar.
    def fechar_resultados():
        janela_resultados.destroy()

    button_fechar = tk.Button(frame_resultados, text="Fechar", font=("Arial", 14), bg="#FFC000", fg="white", command=fechar_resultados, relief="flat", bd=0, width=10, height=1)
    button_fechar.pack(pady=(10, 0))

    janela_resultados.mainloop()
