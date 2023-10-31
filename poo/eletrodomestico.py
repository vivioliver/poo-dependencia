class Eletrodomestico:
    def __init__(self, ligado, voltagem, consumo):
        self.ligado = ligado
        self.voltagem = voltagem
        self.consumo = consumo

    #configurar valor
    def set_valor_voltagem(self, novo_voltagem):
        self.voltagem = novo_voltagem
        #return voltagem

    #retornar valor_voltagem
    def get_valor_voltagem(self):
        return self.voltagem

    #configurar consumo
    def set_valor_consumo(self, consumo):
        self.consumo = consumo
        #return consumo

    #configurar valor_consumo
    def get_valor_consumo(self):
        return self.voltagem


eletr = Eletrodomestico(False, 110, 150)
eletr.set_valor_voltagem(520)
print(eletr.get_valor_voltagem())
eletr.set_valor_consumo(110)
print(eletr.get_valor_consumo())