with open('entrevistados.txt', 'w') as arquivo:
    for i in range(1, 5):
        numero = str(input('Qual o número da sua casa? '))
        cor = str(input('Qual a cor da sua casa? '))
        comodos = str(input('Quantos cômodos tem sua casa? '))
        arquivo.write(numero)
        arquivo.write(cor)
        arquivo.write(comodos)