import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
<<<<<<< HEAD
=======
from PIL import Image, ImageTk
>>>>>>> 8c8d8ebe825773e1f61da9b10c817609e6e3ca84
import random

class Pergunta:
    def __init__(self, pergunta, opcoes, resposta, dica):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta = resposta
        self.dica = dica

class QuizApp:
    def __init__(self, master, perguntas):
        self.master = master
        self.master.title("Quiz Interativo")
        self.perguntas = perguntas
        self.pontuacao = 0
        self.pergunta_atual = None
        self.contagem_regressiva = 10
        self.resposta_escolhida = None

        self.label_pontuacao = tk.Label(self.master, text="Pontuação: 0", font=("Arial", 12))
        self.label_pontuacao.pack(pady=5)

        self.barra_progresso = ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate")
        self.barra_progresso.pack(pady=5)

        self.label_contagem_regressiva = tk.Label(self.master, text="Tempo restante: ", font=("Arial", 10))
        self.label_contagem_regressiva.pack(pady=5)

        self.label_pergunta = tk.Label(self.master, text="", font=("Arial", 12))
        self.label_pergunta.pack(pady=10)

        self.opcoes_var = tk.StringVar()
        self.opcoes_radio = []
        for i in range(4):
            opcao_radio = tk.Radiobutton(self.master, text="", variable=self.opcoes_var, value="", command=self.selecionar_resposta)
            opcao_radio.pack()
            self.opcoes_radio.append(opcao_radio)

        self.botao_ajuda = tk.Button(self.master, text="Dica", command=self.mostrar_dica)
        self.botao_ajuda.pack(pady=10)

        self.botao_proxima_pergunta = tk.Button(self.master, text="Próxima Pergunta", command=self.proxima_pergunta)
        self.botao_proxima_pergunta.pack(pady=10)

        self.proxima_pergunta()

    def proxima_pergunta(self):
        if self.perguntas:
            self.pergunta_atual = random.choice(self.perguntas)
            self.iniciar_contagem_regressiva()
            self.atualizar_interface()
        else:
            self.mostrar_resultado()

    def atualizar_interface(self):
        self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
        self.barra_progresso['value'] = 100
        self.label_contagem_regressiva.config(text="Tempo restante: 10")
        self.label_pergunta.config(text=self.pergunta_atual.pergunta)

        opcoes = self.pergunta_atual.opcoes
        random.shuffle(opcoes)
        for i in range(4):
            self.opcoes_radio[i].config(text=opcoes[i], value=opcoes[i])

    def selecionar_resposta(self):
        self.resposta_escolhida = self.opcoes_var.get()

    def iniciar_contagem_regressiva(self):
        self.contagem_regressiva = 10
        self.atualizar_contagem_regressiva()

    def atualizar_contagem_regressiva(self):
        self.label_contagem_regressiva.config(text=f"Tempo restante: {self.contagem_regressiva}")
        if self.contagem_regressiva > 0:
            self.contagem_regressiva -= 1
            self.master.after(1000, self.atualizar_contagem_regressiva)
        else:
            self.verificar_resposta()

    def verificar_resposta(self):
        if self.resposta_escolhida == self.pergunta_atual.resposta:
            self.pontuacao += 1
            feedback = "Resposta correta!"
        else:
            feedback = f"Resposta incorreta. A resposta correta é: {self.pergunta_atual.resposta}"

        messagebox.showinfo("Feedback", feedback)
        self.perguntas.remove(self.pergunta_atual)
        self.proxima_pergunta()

    def mostrar_dica(self):
        dica = self.pergunta_atual.dica
        messagebox.showinfo("Dica", dica)

    def mostrar_resultado(self):
        resultado = f"Sua pontuação final: {self.pontuacao}/{len(perguntas)}"
        messagebox.showinfo("Resultado", resultado)
        self.master.destroy()

<<<<<<< HEAD
perguntas = [
    Pergunta("Quem é considerado o pai da teoria da relatividade?", ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Niels Bohr"], "Albert Einstein", "Albert Einstein revolucionou a compreensão do tempo, espaço e gravidade."),
    
    Pergunta("Qual foi o evento que deu início à Primeira Guerra Mundial?", ["Ataque a Pearl Harbor", "Afundamento do RMS Lusitania", "Assassinato do Arquiduque Francisco Ferdinando", "Tratado de Versalhes"], "Assassinato do Arquiduque Francisco Ferdinando", "O assassinato do Arquiduque Francisco Ferdinando em Sarajevo desencadeou o conflito global."),
    
    Pergunta("Qual filme ganhou o Oscar de Melhor Filme em 1994?", ["O Pianista", "A Lista de Schindler", "Forrest Gump", "O Rei Leão"], "Forrest Gump", "Forrest Gump, dirigido por Robert Zemeckis, foi o vencedor do Oscar de Melhor Filme em 1994."),
    
    Pergunta("Qual é o país mais populoso do mundo?", ["Estados Unidos", "China", "Índia", "Rússia"], "China", "A China é o país mais populoso, com uma vasta população."),
    
    Pergunta("Quem pintou 'Noite Estrelada'?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Vincent van Gogh", "A 'Noite Estrelada' é uma obra-prima de Vincent van Gogh, famoso por seu estilo único."),
    
    Pergunta("Qual banda britânica é conhecida como os 'Fab Four'?", ["The Rolling Stones", "The Who", "The Beatles", "Queen"], "The Beatles", "The Beatles, também conhecidos como os 'Fab Four', foram uma banda icônica."),
    
    Pergunta("Qual é o título do primeiro livro da série 'Harry Potter'?", ["Harry Potter e a Pedra Filosofal", "Harry Potter e o Prisioneiro de Azkaban", "Harry Potter e a Ordem da Fênix", "Harry Potter e as Relíquias da Morte"], "Harry Potter e a Pedra Filosofal", "O primeiro livro é 'Harry Potter e a Pedra Filosofal'."),
    
    Pergunta("Qual país sediou os Jogos Olímpicos de Verão em 2016?", ["Rússia", "Estados Unidos", "Brasil", "China"], "Brasil", "O Brasil foi o país anfitrião dos Jogos Olímpicos de Verão em 2016."),
    
    Pergunta("Quem é o co-fundador da Microsoft, juntamente com Bill Gates?", ["Steve Jobs", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen"], "Paul Allen", "Paul Allen foi co-fundador da Microsoft ao lado de Bill Gates."),
    
    Pergunta("Qual é o único planeta do sistema solar que gira no sentido horário?", ["Marte", "Júpiter", "Vênus", "Urano"], "Vênus", "Vênus é o único planeta que tem rotação retrógrada, girando no sentido horário."),
=======
# Exemplo de perguntas (substitua por suas próprias perguntas)
perguntas = [
    Pergunta("Qual é a capital do Brasil?", ["Rio de Janeiro", "São Paulo", "Brasília", "Belo Horizonte"], "Brasília", "A cidade foi construída para ser a capital do Brasil."),
    Pergunta("Qual é o maior planeta do sistema solar?", ["Vênus", "Marte", "Júpiter", "Saturno"], "Júpiter", "Este planeta é famoso por suas faixas de nuvens coloridas."),
    Pergunta("Quem escreveu 'Dom Quixote'?", ["Miguel de Cervantes", "William Shakespeare", "Jane Austen", "Charles Dickens"], "Miguel de Cervantes", "Este autor espanhol é conhecido por sua obra-prima 'Dom Quixote'."),
>>>>>>> 8c8d8ebe825773e1f61da9b10c817609e6e3ca84
]

root = tk.Tk()
app = QuizApp(root, perguntas)
root.mainloop()