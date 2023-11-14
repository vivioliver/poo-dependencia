class Integrante_IFRN:
    def __init__(self, exibirMensagem):
        self.exibirMensagem = exibirMensagem

class Professor(Integrante_IFRN):
    def __init__(self, exibirMensagem):
        super().__init__(exibirMensagem)
        self.exibirMensagem = exibirMensagem

class Aluno(Integrante_IFRN):
    def __init__(self, exibirMensagem):
        super().__init__(exibirMensagem)
        self.exibirMensagem = exibirMensagem

i = Integrante_IFRN("Seja bem vindo(a) ao IFRN!!!")
print(i)
p = Professor("Meus alunos são os melhores!!!")
print(p)
a = Aluno("Vou estudar pra tirar 100 em POO!!!")
print(a)