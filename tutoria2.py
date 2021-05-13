#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

#funcion: es una serie de instrucciones o acciones que queremos hacer para obtener un resultado
#hola soy juan

''''
Tipos de variable o datos
String = cadena de caracteres =  cualquier letra o numero o simbolo entre COMILLAS ( ' ' " ")
Float = número CON DECIMALES
int = numero positivo o negativo NO DECIMAL
booleana = logica que nos dice si algo es verdadero o falso, por lo tanto binaria osea que solo puede contener 2 valores
'''

'''
operador = nos permite hacer operaciones = permite realizar acciones entre variables o tipos de datos
Tipos de operadores
+  = suma 
-  = resta
*  = multiplicaciones
/  = division
** = exponencial
%  = residuo
'''
'''
operadores logicos
y = and = incluye interseccion de conuntos (en pocas palabras esta en uno Y en el otro): significa que las operaciones que se estan union por la conjuncion Y o AND se cumplen o son verdaderas
o = OR = significa que cuando unios 2 operaciones por la operacion O o OR solo se necesita que 1 sea verdadera
negacion 
==
>
>=
!=
<=
<
'''

def determinarSiDigitosSonPares():
    numeroEntero = input('Ingrese el número de 2 digitos entero a evaluar: ')
    #validamos si el numero tiene 2 digitos
    if int(numeroEntero) >= 0 and not int(numeroEntero) >= 100:
        # a = int((numeroEntero % 100) / 10)
        # b = int((numeroEntero % 10) / 1)
        # print(a)
        # print(b)
        # print(numeroEntero[0])
        # print(numeroEntero[1])
        primerDigito = int(numeroEntero[0])
        segundoDigito = int(numeroEntero[1])
        primerPar = primerDigito % 2
        segundoPar = segundoDigito % 2
        if primerPar == 0 and segundoPar == 0:
            print(f"Los números  {primerDigito} y {segundoDigito}  son pares")
        else:
            print("Al menos 1 de los 2 dígitos ingresados es impar")
    else:
        print('El numero ingresado no tiene 2 digitos')

determinarSiDigitosSonPares()


