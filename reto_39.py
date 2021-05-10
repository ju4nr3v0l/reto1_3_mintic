''''
MATEMATICA: 2 Quices 50% - 1 Parcial 50%.
FISICA: 3 Quices 45% - 1 Parcial 55%.
QUIMICA: 2 Trabajos 30% - 2 Quices 20% - 1 Parcial 50%.
'''
# float
# string: 'juan es un compañero'
# diccionario -> dic() ejm: { "nombre":"juan","edad":26 }
# “El estudiante
# {nombre} obtuvo las siguientes notas: matemáticas: {nota}, física {nota}, química {nota}”

estudiante = {
"nombre": "Ricardo", # Nombre del estudiante
"mqui1": 75, # Nota del primer quiz matemática (0 – 100)
"mqui2": 60, # Nota del segundo quiz matemática (0 – 100)
"mpar1": 80, # Nota del primer parcial matemática (0 – 100)
"fqui1": 75, # Nota del primer quiz física (0 – 100)
"fqui2": 60, # Nota del segundo quiz física (0 – 100)
"fqui3": 60, # Nota del tercer quiz física (0 – 100)
"fpar1": 80, # Nota del primer parcial física (0 – 100)
"qtra1": 75, # Nota del primer trabajo Química (0 – 100)
"qtra2": 60, # Nota del segundo trabajo Química (0 – 100)
"qqui1": 60, # Nota del primer quiz Quimica (0 – 100)
"qqui2": 80, # Nota del segundo quiz Quimica (0 – 100)
"qpar1": 50 # Nota del primer parcial Quimica (0 – 100)
}
def calcularNotas(estudiante : dict)-> str:
    notaMatematicas = (((estudiante['mqui1'] + estudiante['mqui2']) /2)*0.5) + (estudiante['fqui1']*0.5)
    notaFisica = (((estudiante['fqui1'] + estudiante['fqui2'] +estudiante['fqui3'])/3) *0.45) + (estudiante['fpar1']*0.55)
    notaQuimica = (((estudiante['qtra1'] + estudiante['qtra2'])/2)*0.3) + (((estudiante['qqui1'] + estudiante['qqui2'])/2)*0.2) + (estudiante['qpar1'] * 0.5)
    return f"El estudiante {estudiante['nombre']} obtuvo las siguientes notas: matemáticas: {notaMatematicas}, física {notaFisica}, química {notaQuimica}"


