import tkinter as tk

class JogoLabirinto:
    def __init__(self, master, labirinto):
        self.master = master
        self.master.title("Jogo de Labirinto")
        self.labirinto = labirinto
        self.tamanho_bloco = 30
        self.iniciar_posicao_jogador()

        self.canvas = tk.Canvas(self.master, width=len(labirinto[0]) * self.tamanho_bloco, height=len(labirinto) * self.tamanho_bloco)
        self.canvas.pack()

        self.desenhar_labirinto()
        self.desenhar_jogador()

        self.master.bind("<Up>", lambda e: self.mover_jogador(0, -1))
        self.master.bind("<Down>", lambda e: self.mover_jogador(0, 1))
        self.master.bind("<Left>", lambda e: self.mover_jogador(-1, 0))
        self.master.bind("<Right>", lambda e: self.mover_jogador(1, 0))

    def iniciar_posicao_jogador(self):
        for i, linha in enumerate(self.labirinto):
            if 'S' in linha:
                self.posicao_jogador = [linha.index('S'), i]
                break

    def desenhar_labirinto(self):
        for linha in range(len(self.labirinto)):
            for coluna in range(len(self.labirinto[linha])):
                cor = "white" if self.labirinto[linha][coluna] == ' ' else "black"
                self.canvas.create_rectangle(coluna * self.tamanho_bloco, linha * self.tamanho_bloco,
                                             (coluna + 1) * self.tamanho_bloco, (linha + 1) * self.tamanho_bloco,
                                             fill=cor)

    def desenhar_jogador(self):
        x, y = self.posicao_jogador
        self.canvas.create_rectangle(x * self.tamanho_bloco, y * self.tamanho_bloco,
                                     (x + 1) * self.tamanho_bloco, (y + 1) * self.tamanho_bloco,
                                     fill="green")

    def mover_jogador(self, dx, dy):
        nova_posicao = [self.posicao_jogador[0] + dx, self.posicao_jogador[1] + dy]
        if 0 <= nova_posicao[0] < len(self.labirinto[0]) and 0 <= nova_posicao[1] < len(self.labirinto):
            if self.labirinto[nova_posicao[1]][nova_posicao[0]] != '#':
                self.canvas.delete("all")
                self.desenhar_labirinto()
                self.posicao_jogador = nova_posicao
                self.desenhar_jogador()

if __name__ == "__main__":
    labirinto = [
        "#########",
        "#S    #  #",
        "#   ##  #",
        "# ##    #",
        "#   ##  #",
        "# ##    #",
        "#   ##  #",
        "#  ##   #",
        "#   G   #",
        "#########"
    ]

    root = tk.Tk()
    jogo = JogoLabirinto(root, labirinto)
    root.mainloop()
