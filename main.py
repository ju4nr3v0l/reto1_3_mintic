### llamamos el metodo que inicia el procedimiento
def comenzar():
    ### creamos variable tipo diccionario para garantizar la estrucutra de dato
    empleado = dict()
    ### solicitamos el input en el tipo de variable esperado para evitar errores y validamos que si se ingrese el dato en la funcion
    empleado['nombre'] = solicitarNombre()
    empleado['horas'] = solicitarHoras()
    empleado['boni'] = solicitarBonificacion()
    calcularPago(empleado)


def calcularPago(empleado: dict):
    horasTotales = calcularHorasyExtras(empleado['horas'])
    valorHorasNormales = horasTotales['normales'] * 3785.00
    valorHorasExtas = horasTotales['extras'] * 4731.00
    auxTransporte = 106454.00/30
    saludPension = -258927.00/30
    # print(horasTotales)
    # print(valorHorasNormales)
    # print(valorHorasExtas)
    # print(auxTransporte)
    # print(saludPension)
    totalPagar = valorHorasNormales + valorHorasExtas + auxTransporte + saludPension + empleado['boni']
    totalPagar = "${:,.2f}".format(totalPagar)
    return print(f"El empleado {empleado['nombre']} total a pagar {totalPagar}")


def validarDiccionario(empleado):
    if 'nombre' in empleado and 'horas' in empleado and empleado['nombre'] != '' and empleado['horas'] != '':
        return True
    else:
        return False


def calcularHorasyExtras(horas):
    horasCalculadas = dict()
    horasExtras = float(horas) - 8.0
    if horasExtras <= 0.0:
        horasCalculadas['normales'] = float(horas)
        horasCalculadas['extras'] = float(0)
    else:
        horasCalculadas['normales'] = float(8)
        horasCalculadas['extras'] = float(horasExtras)
    return horasCalculadas


def solicitarNombre():
    nombre = input("¿cuál es el nombre del empleado? esto es obligatorio ")
    if nombre.isalpha() and nombre != '':
        return nombre
    else:
        print('El valor para nombre es obligatorio y debe usar solo catacteres A-Z a-z')
        solicitarNombre()


def solicitarHoras():
    horas = input("¿cuantas horas trabajo el empleado? (esto es obligatorio y debe ser un número positivo) ")
    if horas.replace(".", "", 1).isdigit() and float(horas) >= 0.0:
        horasReturn = float()
        horasReturn = horas
        return float(horasReturn)
    else:
        print('El valor para horas es obligatorio y debe ser solo números o números con decimales')
        solicitarHoras()


def solicitarBonificacion():
    bonificacion = input("¿recibió alguna bonificación? de ser asi por favor ingrese el valor en dinero sin usar puntos, comas o signo pesos si no tiene bonificación por favor ingrese 0 ")

    if bonificacion.isdigit():
        return float(bonificacion)
    else:
        print('El valor para bonficación debe ser un número con las caracteristicas mencionadas, si no tiene bonificación por favor ingrese 0')
        solicitarBonificacion()

comenzar()