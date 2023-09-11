def calcular_perimetro (lados):
    perimetro = 0
    for i in range(lados):
        valor = int(input('Valor do lado: '))
        perimetro += valor
    return (perimetro)

q_lados = int(input('Quantidade de lados da forma: '))
resultado = calcular_perimetro(q_lados)
print(resultado)