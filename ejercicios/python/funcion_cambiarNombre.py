'''
Escribe una función llamada numerosPrimos. Esta función recibe como parámetro
# un número entero positivo. La función se encarga de crear un arreglo con los
# números primos desde el 1 hasta el número proporcionado. La función retorna
# el arreglo como resultado.
# 13 => [2, 3, 5, 7, 11]
'''

def esPrimo(numeroIterador):
    contador = 0
    for x in range (1, numeroIterador+1):
        if numeroIterador % x == 0:
            contador += 1
    if contador == 2:
        #print("VINO ACA")
        return True
    else:
        return False
   

def numeroPrimo(numero):
    arreglo = []
    for i in range(1,numero):
        #llamar a la funcion que indica si es primo esprimo(i)
        if esPrimo(i) == True:
            arreglo.append(i)
    return arreglo

        #if i % 2 != 0:
        #    arreglo.append(i)
    #return arreglo

#print(numeroPrimo(13))




x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# Camia el valor 10 en x a 15
valorCambio = x[1][0]
print(valorCambio, "ESTE VALOR DEBO CAMBIAR")
print(x, "LISTA X INICIAL")
x[1][0] = 15
print(x, 'LISTA X ACTUALIZADA')

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print(estudiantes[0]['last_name'])
print(estudiantes, 'ESTUDIANTES ACTUAL')
estudiantes[0]['last_name'] = "Bryant"
print(estudiantes, 'ESTUDIANTES ACTUALIZADO')

#Cambia el valor 20 en z a 30.

print(len(z))
z[0]['y'] = 30
print(z)
print(len(z[0]))


# En el directorio_deportes, cambia "Messi" por "Andrés".
'''
print(directorio_deportes['fútbol'][0])
directorio_deportes['fútbol'][0] = "Andrés"
print(directorio_deportes)
'''

def cambiarNombre(diccionario):
    for nombre in diccionario:
        for i in diccionario[nombre]:
            #print(i, "ES MESSI")
            if i == "Messi" :
                indiceMessi = diccionario[nombre].index('Messi')
                print(indiceMessi , "INDICE MESSI?")
                diccionario[nombre][indiceMessi] = "Andrés"

    return diccionario

print(directorio_deportes, "LISTA DEPORTES INICIAL" )
print(cambiarNombre(directorio_deportes), "RESULTADO DE CAMBIAR NOMBRE")    

#REVISAR ALGORITMOS