# adulto = 12000
# menores = 10000
# descuento 1 = 10% si son 2 boletas,
# descuento 2 = 15%si son 3 boletas
# descueto 3 = 20% si son 4 boletas.

def calcularValorApagar(adultos, menores):
    totalAdultos = adultos * 12000
    totalMenores = menores * 10000
    totalAsistentes = adultos + menores
    if totalAsistentes == 2:
        totalAdultos = totalAdultos * 0.9
        totalMenores = totalMenores * 0.9
    if totalAsistentes == 3:
        totalAdultos = totalAdultos * 0.85
        totalMenores = totalMenores * 0.85
    if totalAsistentes == 4:
        totalAdultos = totalAdultos * 0.8
        totalMenores = totalMenores * 0.8

    totalPagar = totalAdultos + totalMenores
    return print(f"El valor a pagar por adultos es: {totalAdultos} y por menores es: {totalMenores} para un total a pagar de: {totalPagar}.")


# calcularValorApagar(1,2)

