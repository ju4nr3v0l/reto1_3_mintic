'''
km <= 300 -> $300.000
km > 300 and <= 1000 -> $15.000 por cada km adicional a 300
km > 1000 -> $10.000 por cada km

determinar el valor por concepto de alquiler y el valor del IVA = 16%

kilometros float
"El monto a pagar es de “monto” y la cantidad de iva es “iva”"
'''

'''
#### tipos de variables
enteras = int: un número NO DECIMAL
flotantes = float: un número DECIMAL 
cadena de texto = string(str): numeros , letras, simbolos estan contenidos dentro de comillas ('', "") 
booleanas = bool: solo contiene los valores de True o False o Verdadero o Falso - binaria.
= 0 - 1
diccionario = estructurada de tipo LLAVE : VALOR {"nombre":"juan"}
'''
'''
if = pregunta
### operadores lógicos
> : mayor que
>= : mayor o igual
== : igual -> valida valores
!= : distinto
negacion not: 
=== : validar valores -> valida tipo de dato
Y - and : conjunción-> se necesita que todas las condiciones UNIDAS por la CONJUNCION se cumplan para ser verdad
O - or  : disyunción-> se necesita que al menos UNA de las afirmaciones se cumpla para ser verdadero
'''
'''
while = ciclo-logico
for
foreach
swiche
'''
'''
FUNCION: serie de instrucciones que se implementan para obtener o procesar un resultado
'''
def alquiler(kilometros: float)->str:
    if kilometros <= 300:
        monto = 300000
    else:
        if kilometros <= 1000:
            monto = 300000
            kilometrosExceso300 = kilometros - 300
            valorKilometrosExceso300 = kilometrosExceso300 * 15000
            monto = monto + valorKilometrosExceso300
        else:
            kilometrosEncimaDe1000 = kilometros - 1000
            valorKilometrosEncima1000 = kilometrosEncimaDe1000 * 10000
            kilometrosExceso300 = kilometros - kilometrosEncimaDe1000 - 300
            valorKilometrosExceso300 = kilometrosExceso300 * 15000
            tarifa300 = 300000
            monto = valorKilometrosEncima1000 + valorKilometrosExceso300 + tarifa300
    iva = monto * 0.16
    return f"El monto a pagar es de {monto} y la cantidad de iva es {iva}"

print(alquiler(301))


