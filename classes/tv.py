class Eletrodomestico:
    def __init__(self, ligado, voltagem, consumo):
        self.ligado=ligado
        self.voltagem=voltagem
        self.consumo=consumo

    def isLigado(self):
        return(self.ligado)

    def setLigado(self, ligado):
        self.ligado=ligado

class TV(Eletrodomestico):
    def __init__(self, ligado, voltagem, consumo, canal, volume, tamanho):
        super().__init__(ligado, voltagem, consumo)
        self.canal=canal
        self.volume=volume
        self.tamanho=tamanho

    def setVolume(self, volume):
        self.volume=volume

    def isVolume(self):
        return(self.volume)

    def setTamanho(self, tamanho):
        self.tamanho=tamanho

    def isTamanho(self):
        return(self.tamanho)