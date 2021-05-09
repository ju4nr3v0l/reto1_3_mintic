#horas normales = 3785
#horas extras = 4731
#+auxilio transporte mensual = 106454/30
#+ bonificaciones = ingresadas por el usuario
#-salud y pensión mensual: 258927/30


def calcularPago(empleado:dict)->dict:
    horasExtras =  empleado['horas'] - 8
    horasNormales = empleado['horas'] - horasExtras
    if horasExtras < 0:
        horasExtras = 0
        horasNormales = empleado['horas']
    valorPagar = horasExtras*4731 + horasNormales*3785
    auxTransporteDia = 106454/30
    saludPensionDia = 258927/30
    totalPagar = (valorPagar + auxTransporteDia + empleado['boni']) - saludPensionDia
    totalPagar = round(totalPagar,2)
    return f"El empleado {empleado['nombre']} total a pagar {totalPagar}"

empleado = {"nombre": "Ricardo","horas": 6,"boni":0 }

calcularPago(empleado)
