carros = 100
espacio_entre_carros = 4.0
conductores = 30
pasajeros = 90
carros_no_conducidos = carros - conductores
carros_conducidos = conductores
capacidad_loteCarros = carros_conducidos * espacio_entre_carros
promedio_pasajeros_por_carros = pasajeros / carros_conducidos

#Mensajes que serán presentados
#(git commit -am "texto") --> para agregar ultimos cambios
#Otro comentario
print("Existen ", carros, " carros disponibles.")
print("Solo hay ", conductores, " conductores.")
print("Deben haber ",carros_no_conducidos," carros vacios hoy.")
print("Podemos transportar ",capacidad_loteCarros," personas hoy.")
print("Tenemos ",pasajeros," pasajeros hoy.")
print("Necesitamos hoy poner ",promedio_pasajeros_por_carros," pasajeros en cada carro.")