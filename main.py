import funciones

### llamamos el metodo que inicia el procedimiento
def comenzar():
    ### creamos variable tipo diccionario para garantizar la estrucutra de dato
    empleado = dict()
    ### solicitamos el input en el tipo de variable esperado para evitar errores y validamos que si se ingrese el dato en la funcion
    empleado['nombre'] = funciones.solicitarNombre()
    empleado['horas'] = funciones.solicitarHoras()
    empleado['boni'] = funciones.solicitarBonificacion()
    funciones.calcularPago(empleado)

comenzar()