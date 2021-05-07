#baldosa
#Ancho:40 cm
#Largo:60 cm
#piso
#Ancho: 346 cm
#Largo: 495 cm
### > = mayor que < = menor que  == =igual & = Y || = ó (! , not , ¬) = negación # operadores logicos
# IF ELSE
# p =  esta lloviendo
# q = esta haciendo sol
# p && q = es verdadera
# p = true || q = false = verdadera
#### tipos de datos
# entero = int = 100
# flotante = float = 1.123456789
# booleano = bool = Verdadero y Falso True o False
# Cadena de texto = string = "hola mi nombre es juan"
# diccionario = dict = {"oscar": 100,"vladimir":200, "juan": 0 } = dict['oscar']
#

def calcularBaldosasNecesarias():
    areaBaldosa = calcularArea(40, 60)
    areaCuarto = calcularArea(346, 495)
    baldosasNecesarias = areaCuarto / areaBaldosa
    print(baldosasNecesarias)
    return print(f"Es necesario adquirir {int(baldosasNecesarias)} baldosas")

def calcularArea(ancho,largo):
    area = ancho * largo
    return area

calcularBaldosasNecesarias()
# def testDiccionario():
#     celular = {"marca":"samsung","medida":150,"pantalla":"amoled", "memoria":"2G"}
#     print(celular)
# testDiccionario()





