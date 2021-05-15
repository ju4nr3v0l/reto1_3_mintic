#Leer un número entero y determinar si es un número terminado en 4.
#1- Leer un numero
#2- validar si es entero
#3- determinar si termina en 4
'''
#### tipos de datos
enteros ó int = debe ser un NUMERO y NO  debe ser DECIMAL
string ó cadena texto = secuencia de caracteres (numeros - letras - simbolos) estan delimitados por  '' " "
flotantes o float = deber se un NUMERO y DEBE TENER DECIMALES
booleanos o bool = puede ser verdadero o falso (binario) True o False 1 y 0
listas = secuencia de datos de multiples tipos o un solo separados por ,
diccionario = es una secuencia de datos ESTRUCTURADA (2 elementos) en asignacion por LLAVE -> VALOR {"llave":"valor"}
############
##### OPERADORES ######
suma = + adiciona valores
resta = - sustrae valores
Multiplicacion = *
Division = /
Exponencial = **
Modulo o mod = % : Residuo (lo que sobra) de una division  5 % 4
> : mayor -> valida una comparacion de tamaño en valores numericos
< : menor -> valida una comparacion de tamaño en valores numericos
>= : mayor o igual -> valida una comparacion de tamaño en valores numericos
<= : menor o igual -> valida una comparacion de tamaño en valores numericos
!= : diferente -> determinar si NO SON IGUALES (Valores, propiedades, booleanos)
== : igualdad -> determinar si SON IGUALES (Valores, propiedades, booleanos)
=== : igualdad estricta -> Determina si un valor Y TIPO DE DATO son iguales
and o Y: conjuncion -> Valida si TODOS los datos unidos por una conjuncion se cumplen
Ó o or: disyunción  -> Valida si AL MENOS UNO de los datos unidos por una dinyuncion se cumple
not : negación " NO es por la mañana O NO estamos en tutoria"
##########
if o SI : condicional -> Pregunta
########
funcion : una serie de instrucciones o PASOS que pueden ser reutilizados,
retorna un resultado, puede recibir datos iniciales o parámetros
'''
#### parametro: valor de entrada a una función ES VARIABLE - CONSTANTE
def validarNumeroTerminaEnCuatro(numero: int)->str:
    if isinstance(numero,int):
        numero = str(numero)
        test = numero[len(numero) -1]
        if int(test) == 4:
            return 'El número ingresado termina en 4'
        else:
            return 'El número ingresado NO termina en 4'
    else:
        return "El número ingresado no es un entero"

print(validarNumeroTerminaEnCuatro(12444))
